// Funcoes e inicializacoes


// Initialize collapsible (uncomment the lines below if you use the dropdown variation)
// var collapsibleElem = document.querySelector('.collapsible');
// var collapsibleInstance = M.Collapsible.init(collapsibleElem, options);

//$(".dropdown-trigger").dropdown();

/*document.addEventListener('DOMContentLoaded', function() {
	var elems = document.querySelectorAll('.sidenav');
	var instances = M.Sidenav.init(elems, options);
});*/

// Or with jQuery

// Simulation data dictionary


var bin2unsigned = function(bin){

	var lennumb = bin.length-1 //len(binnumb)-1
	var unumb = 0
	for(var i=0; i<bin.length; i++){
		unumb = unumb + 2**lennumb * parseInt(bin[i]);
		lennumb = lennumb-1;
	} 
	return unumb;
}

var bin2signed = function(bin){
	snumb = bin2unsigned(bin)
	if(bin[0] == '1'){

		return snumb - 2**bin.length;
	}
	//console.log(snumb);
	return snumb;
	
}

var convert_data = function(n,base,pad,sign){

	aux = n.toString(base)
	if(aux.length<=pad){
		pad_n = pad-aux.length;
	}
	return(sign.repeat(pad_n)+aux);

}




var register_values_to_json = function(){
	
	registers_json = {};

	for( i=0; i<32; i++){
		register_number = i.toString(2)
		if(register_number.length<5){
			pad = 5 - register_number.length;
			register_number = "0".repeat(pad)+register_number;
		}

		registers_json[convert_data(i,2,5,"0")] = program_data['registers'][register_number];
		
		

	}	
	//console.log(registers_json);
	return registers_json;

};

//console.log(register_values_to_json());

// global variable
var program_data;
var initialize_program_data = function(){


	// inicializa registradores
	var registers = {};
	for(var i=0; i<32; i++){
		registers[convert_data(i,2,5,"0")] = convert_data(0,16,8,"0");
		
	};
	if(  $("input[name=simulation_registers_format]:checked").attr("id") == "simulation_registers_format_hex"  ){
    	for(var i=0; i<32; i++){        		
    		$("#reg_x"+i+"_val").html("0x"+registers[convert_data(i,2,5,"0")]);
    	};
	}else if(  $("input[name=simulation_registers_format]:checked").attr("id") == "simulation_registers_format_dec"  ){
    	for(var i=0; i<32; i++){        		
			$("#reg_x"+i+"_val").html("0");
		};
	}


	// Inicializa mapa de memoria
	var memory_map_table_rows_current = $("#memory_map_table_rows").html("");
	for(var i=0; i<64; i=i+16 ){
		var memory_map_table_rows_current = $("#memory_map_table_rows").html();

		$("#memory_map_table_rows").html(memory_map_table_rows_current
				+"<tr>"
					+"<td id=\"mem_pos_"+i+"_title\"><b>0x"+convert_data(i,16,8,"0")+"</b></td>"
					+"<td id=\"mem_pos_"+(i+12)+"\" contenteditable>0x00000000</td>"
					+"<td id=\"mem_pos_"+(i+8)+"\" contenteditable>0x00000000</td>"
					+"<td id=\"mem_pos_"+(i+4)+"\" contenteditable>0x00000000</td>"
					+"<td id=\"mem_pos_"+i+"\" contenteditable>0x00000000</td>"
				+"</tr>");

	}

	// Inicializa bitmap blocks
	$("#blocks_container").html("");
	for(var i=0; i<16; i++){
		$("#blocks_container").append("<div id='linha"+i+"' class='block_row'></div>");
		for(var j=0; j<16; j++){
			block_mem_addr = (256+((16*i+j)*4));
			$("#linha"+i).append("<div id='block_mem_addr_"+block_mem_addr.toString(16)+"'' class='block'></div>");
		}
		
	}

	$("#simulation_output_screen").html(">>");

	program_data = {
		"code" : "",
		"memory" : "",
		"registers": registers,
		"program_counter": 0,
		"console_input": "",
		"console_output": ""
	}

	$(".assembled_info").css("background-color","white");
	$("#assembled_info_pc_"+program_data['program_counter']).css("background-color","#ffff99");

};
initialize_program_data();


var assemble = function(){
	$("#code").html("")
  	$("#errors").html("")
  	$("#memory").html("")

  	//console.log(editor.getValue())

    $.post("/assemble",{code:editor.getValue()}, function(data, status){
        if (status == "success"){
        	
        	assmblr_response = JSON.parse(data);

        	code = assmblr_response['code'];
        	memory = assmblr_response['memory'];
        	errors = assmblr_response['errors'];
        	
        	if( errors == "" ){
        		$("#run_button").removeClass("disabled");
        		$("#step_button").removeClass("disabled");
        		$("#auto_run_button").removeClass("disabled");
        	}else{
        		$("#run_button").addClass("disabled");
        		$("#step_button").addClass("disabled");
        		$("#auto_run_button").addClass("disabled");
        	}
        	data_format = $("input[name=format_input_radio]:checked")[0].value
        	
        	display_data("code", code[data_format], data_format);
        	display_data("memory", memory[data_format], data_format);
        	display_data("errors", errors,data_format);

        	//console.log(assmblr_response);
        	
        	$("#simulation_assembled_info").html("")
        	table_sim_info = $("#simulation_assembled_info")
			$.each(assmblr_response['assembled_info'],function(index, value){
			    table_sim_info.append("<tr class='assembled_info' id='assembled_info_pc_"+value['pc']+"'><td>"+value['pc']+"</td><td>"+value['hex']+"</td><td>"+value['instr']+"</td></tr>") 
			    //console.log(value['pc']);
			    //console.log(value['hex']);
			    //console.log(value['instr']);
			});

        	program_data = {
        		"code" : code["bin"],
        		"memory" : memory["bin"],
        		"registers": register_values_to_json(),
				"program_counter": 0,
				"console_input": "",
				"console_output": ""
        	}
        	
			$(".assembled_info").css("background-color","white");
			$("#assembled_info_pc_"+program_data['program_counter']).css("background-color","#ffff99");

        }	        

		//console.log(program_data['registers']);

});
}



var auto_scroll = function(){

	assmb_ht = $("#simulation_assembled_info").height()
	assmb_pos = $("#simulation_assembled_info").offset().top
	info_pc_curr_pos = $("#assembled_info_pc_"+program_data['program_counter']).offset().top

	//console.log(assmb_ht)
	//console.log(assmb_pos)
	//console.log(info_pc_curr_pos)
	//console.log(program_data['program_counter'])
	//console.log(program_data['program_counter']/4)

	//console.log("---------------")
	if (info_pc_curr_pos <= assmb_pos+20){
		//console.log("111111");
		$("#simulation_assembled_info")[0].scrollTo(0, 30*((program_data['program_counter']/4)-1));
		//$("#simulation_assembled_info")[0].scrollTo(0, assmb_pos);
	}  

	if(info_pc_curr_pos > assmb_ht+assmb_pos-20){
		//console.log("222222");
		$("#simulation_assembled_info")[0].scrollTo(0, 30*(program_data['program_counter']/4));
		//$("#simulation_assembled_info")[0].scrollTo(0, assmb_ht+assmb_pos);
	}	
}


var run_simulation = function(step_count){
	//console.log(JSON.stringify(program_data['code']))
	//console.log(JSON.stringify(program_data['memory']))
	
	program_data['registers'] = register_values_to_json();
	//console.log(JSON.stringify(program_data['registers']) );
	//console.log(program_data['registers']);
	
	simulation_info = {
						code: 				JSON.stringify(program_data['code']),
						memory: 			JSON.stringify(program_data['memory']),
						registers: 			JSON.stringify(program_data['registers']),
						program_counter: 	JSON.stringify(program_data['program_counter']),
						console_input: 		JSON.stringify(program_data['console_input']),
						console_output:		JSON.stringify(program_data['console_output']),
						step_count: 		step_count							
					}

	$.post("/run", simulation_info, function(data, status){
		//console.log(program_data['registers']);
        if (status == "success"){
        	
        	simulator_response = JSON.parse(data);
        	//$("#simulation_registers").html(simulator_response['registers'])
        	//console.log(simulator_response);


			// Popular dados de registradores
        	for( i=0; i<32; i++){
        		register_number = i.toString(2)
        		if(register_number.length<5){
        			pad = 5 - register_number.length;
        			register_number = "0".repeat(pad)+register_number;
        		}
        		//$("#reg_x"+i+"_val").html("0x"+simulator_response['registers'][register_number]);
        		if(  $("input[name=simulation_registers_format]:checked").attr("id") == "simulation_registers_format_dec"  ){
        			$("#reg_x"+i+"_val").html(bin2signed(simulator_response['registers'][register_number]));
        		}else{
        			$("#reg_x"+i+"_val").html("0x"+convert_data(parseInt(simulator_response['registers'][register_number], 2), 16,8,"0") );
        		}
        		program_data['registers'][register_number] = simulator_response['registers'][register_number];
        		

        	}

        	
        	// popula dados da memoria
			$("#memory_map_table_rows").html("");

			for(var i = 0; i < simulator_response['memory_map'].length; i = i + 16 ){
				memory_map_table_rows_current = $("#memory_map_table_rows").html()

				var k = 0;
				memory_cell = [];
				for( var j=i; j<i+16; j=j+4){

					memory_cell[i+k] = simulator_response['memory_map'][j+3] +
										simulator_response['memory_map'][j+2] + 
										simulator_response['memory_map'][j+1] + 
										simulator_response['memory_map'][j];

					k = k + 1;
					
				}
				if( $("input[name=simulation_memmap_format]:checked").attr("id") == "simulation_memmap_format_dec"  ){

					$("#memory_map_table_rows").html(memory_map_table_rows_current
						+"<tr>"
							+"<td id=\"mem_pos_"+i+"_title\"><b>0x"+convert_data(i,16,8,"0")+"</b></td>"
							+"<td id=\"mem_pos_"+i+12+"\" contenteditable>"+ bin2signed(memory_cell[i+3]) +"</td>"
							+"<td id=\"mem_pos_"+i+8+"\" contenteditable>"+  bin2signed(memory_cell[i+2]) +"</td>"
							+"<td id=\"mem_pos_"+i+4+"\" contenteditable>"+  bin2signed(memory_cell[i+1]) +"</td>"
							+"<td id=\"mem_pos_"+i+"\" contenteditable>"+  bin2signed(memory_cell[i]) +"</td>"
						+"</tr>");
				}else {
					$("#memory_map_table_rows").html(memory_map_table_rows_current
						+"<tr>"
							+"<td id=\"mem_pos_"+i+"_title\"><b>0x"+convert_data(i,16,8,"0")+"</b></td>"
							+"<td id=\"mem_pos_"+i+12+"\" contenteditable>0x"+ convert_data( parseInt(memory_cell[i+3],2),16,8,"0") +"</td>"
							+"<td id=\"mem_pos_"+i+8+"\" contenteditable>0x"+ convert_data( parseInt(memory_cell[i+2],2),16,8,"0") +"</td>"
							+"<td id=\"mem_pos_"+i+4+"\" contenteditable>0x"+ convert_data( parseInt(memory_cell[i+1],2),16,8,"0") +"</td>"
							+"<td id=\"mem_pos_"+i+"\" contenteditable>0x"+ convert_data( parseInt(memory_cell[i],2),16,8,"0") +"</td>"
						+"</tr>");
        	

				}

        	}
        	

			for( var mem_addr_index = 256; mem_addr_index < 1280; mem_addr_index=mem_addr_index+4 ){
				$("#block_mem_addr_"+mem_addr_index.toString(16)).css("background-color","rgb("+simulator_response['memory_map'][mem_addr_index+2]+","+simulator_response['memory_map'][mem_addr_index+1]+","+simulator_response['memory_map'][mem_addr_index]+")")
			}

        	
        	// popula dados do console de output
        	$("#simulation_output_screen").html("");
        	if(simulator_response['console_output'].length == 0){
        		$("#simulation_output_screen").html(">>");
        	}
        	//console.log(simulator_response['console_output']);
        	for(var i=0; i<simulator_response['console_output'].length; i++ ){
        		new_console_line = ">> "+simulator_response['console_output'][i]+"<br>";
        		console_current = $("#simulation_output_screen").html();
        		$("#simulation_output_screen").html(console_current+new_console_line);
        	}
        	program_data['console_output'] = $("#simulation_output_screen").html();
        	
        	program_data['program_counter'] = simulator_response['program_counter'];		      
			$(".assembled_info").css("background-color","white");
			$("#assembled_info_pc_"+program_data['program_counter']).css("background-color","#ffff99");
			auto_scroll();
        	program_data['memory'] = simulator_response['memory_map'];
        	//console.log(program_data['memory']);

        }
    });

} 



//var value = "# RISC-V Assembly Code\n\n.data\n    .asciiz \"texto\"\n\n.text\n    sub x9, zero, 10\n    add x10, ra, a0\n\n    ABCDFEabcdef";
var value = "# RISC-V Assembly Code\n.data\n\tword_teste: .word 26\n\tstr_teste: .asciiz \"\\Hello, World!\\nTesting\\tEscaping!\"\n\n.text\n\tlw x4, x5, word_teste\n\taddi x9, zero, 10\n\taddi x9, zero, -3\n\tadd x10, x9, x4\n\tsw x10,8(x8)";

value = "# RISC-V Assembly Code\n.data\n\tn_fibs: .word 8\n\tfib_base_mem_addr: .word 16\n.text\nfib:\n\tlw x3, n_fibs(x0) # counter\n\taddi x4, x0, 1  # fib number\n\taddi x6, x0, 0 # fib aux\n\n\taddi x10,zero,1\nloop:\n\tbeq x3, x0, end\n\n\tjal x20, print_to_console\n\tjal x21, print_to_mem\n\n\taddi x7, x4, 0 #aux = fib\n\tadd x4, x4, x6  # fib = fib+fib_aux\n\taddi x6,x7,0 # fib_aux = aux\n    \n\taddi x3,x3, -1 #dec counter\n\tjal x0, loop\n\nprint_to_console:\n\taddi x5,x4,0  \n\tecall# print value\n\tjalr x0, x20, 0\n\nprint_to_mem:\n\tsw x4, fib_base_mem_addr(x30)\n\taddi x30, x30, 4\n    jalr x0, x21, 0\n\nend: \n\n"

var editor = CodeMirror(document.getElementById("code-editor"), {
	value: value,
	lineNumbers: true,
	mode: "riscv",
	keyMap: "sublime",
	autoCloseBrackets: true,
	matchBrackets: true,
	showCursorWhenSelecting: true,
	theme: "monokai",
	tabSize: 4,
	autofocus: true
});

var code;
var memory;
var errors;


display_data = function(field,data,data_format){
	if (data == ""){
		$("#"+field).html("No Output")
	}else{
		if (field == "code"){
			for(i=0; i<data.length; i++){
		       	$("#"+field).html($("#"+field).html()+data[i]+"<br>" );	
		    }	
		}else if(field == "memory"){
			if ( data_format == "bin" || data_format == "hex"){
	        	for(i=0; i<data.length-4; i=i+4){
		        		$("#"+field).html($("#"+field).html()+data[i+3]+data[i+2]+data[i+1]+data[i]+"<br>" );	
	        	}
	        }else{
	        	for(i=0; i<data.length; i++){
		        		$("#"+field).html($("#"+field).html()+data[i]+"<br>" );	
	        	}
	        }
		}else if(field == "errors"){
        	for(i=0; i<data.length; i++){
        		$("#"+field).html($("#"+field).html()+errors[i]+"<br>" );	
        	}
		}	
	}
}
