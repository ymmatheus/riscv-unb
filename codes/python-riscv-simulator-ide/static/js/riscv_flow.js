// Eventos e fluxo de telas	

$(document).ready(function(){

	$('.sidenav').sidenav();
	
	$("#entrada").css("display","block");
	$("#saida").css("display","none");
	$("#simulator").css("display","none");
	$("#instructions").css("display","none");
	$("#about_us").css("display","none");

	$("#pause_simulation").css("display", "none");

	$("#bitmap_simulation").css("display", "none");

	// temporary
	$("#bitmap_panel").css("display", "none");

	$("#menu_entrada").click(function(){
		$("#entrada").css("display","block");
		$("#saida").css("display","none");
		$("#simulator").css("display","none");
		$("#instructions").css("display","none");
		$("#about_us").css("display","none");

	});

	$("#run_button").addClass("disabled");
	$("#step_button").addClass("disabled");
	$("#auto_run_button").addClass("disabled");

	$("#menu_saida").click(function(){
		$("#entrada").css("display","none");
		$("#saida").css("display","block");
		$("#simulator").css("display","none");
		$("#instructions").css("display","none");
		$("#about_us").css("display","none");

	});

	$("#menu_simulator").click(function(){
		$("#saida").css("display","none");
		$("#entrada").css("display","none");
		$("#simulator").css("display","block");
		$("#instructions").css("display","none");
		$("#about_us").css("display","none");

	});

	$("#menu_instructions").click(function(){
		$("#saida").css("display","none");
		$("#entrada").css("display","none");
		$("#simulator").css("display","none");
		$("#instructions").css("display","block");
		$("#about_us").css("display","none");

	});


	$("#menu_about").click(function(){
		$("#saida").css("display","none");
		$("#entrada").css("display","none");
		$("#simulator").css("display","none");
		$("#instructions").css("display","none");
		$("#about_us").css("display","block");

	});

	$("#main_panel").click(function(){
		$("#simulation_assembled_code").css("display","block");
		$("#bitmap_simulation").css("display","none");
		$("#simulation_registers").css("display","block");		
		$("#simulation_memory_map").css("display","block");
		$("#simulation_console").css("display","block");
	});

	$("#bitmap_panel").click(function(){
		$("#simulation_assembled_code").css("display","block");
		$("#bitmap_simulation").css("display","block");
		$("#simulation_registers").css("display","none");		
		$("#simulation_memory_map").css("display","block");
		$("#simulation_console").css("display","none");

	});

	$("#run_button").click(function(){
		$("#saida").css("display","none");
		$("#entrada").css("display","none");
		$("#simulator").css("display","block");

		step_count = -1; // runs until the end
		run_simulation(step_count);

	});

	$("#step_button").click(function(){
		$("#saida").css("display","none");
		$("#entrada").css("display","none");
		$("#simulator").css("display","block");

		$(".assembled_info").css("background-color","white");
		$("#assembled_info_pc_"+program_data['program_counter']).css("background-color","#ffff99");
		
		step_count = 1; // runs one step
		run_simulation(step_count);
	});

	var interval_auto_run_id;
	$("#auto_run_button").click(function(){

		$("#saida").css("display","none");
		$("#entrada").css("display","none");
		$("#simulator").css("display","block");
		step_count = 1; // runs one step				
		
		interval_auto_run_id = setInterval(function(){ 
				$(".assembled_info").css("background-color","white");
				$("#assembled_info_pc_"+program_data['program_counter']).css("background-color","#ffff99");
				console.log(step_count);
				run_simulation(step_count);
			}, 500);

		$("#auto_run_simulation").css("display", "none");
		$("#pause_simulation").css("display", "inline");
	});



	$("#assemble_button").click(function(){
		initialize_program_data();
		assemble();
	});

	$("#run_simulation").click(function(){
		step_count = -1; // runs until the end
		run_simulation(step_count);
	});

	$("#step_simulation").click(function(){
		step_count = 1; // runs one step				
		$(".assembled_info").css("background-color","white");
		$("#assembled_info_pc_"+program_data['program_counter']).css("background-color","#ffff99");
		run_simulation(step_count);
	});

	$("#reset_simulation").click(function(){
		initialize_program_data();
		assemble();
	});


	
	$("#auto_run_simulation").click(function(){
		step_count = 1; // runs one step				
		
		interval_auto_run_id = setInterval(function(){ 
				$(".assembled_info").css("background-color","white");
				$("#assembled_info_pc_"+program_data['program_counter']).css("background-color","#ffff99");
				console.log(step_count);
				run_simulation(step_count);
			}, 500);

		$("#auto_run_simulation").css("display", "none");
		$("#pause_simulation").css("display", "inline");
	});

	$("#pause_simulation").click(function(){
		clearInterval(interval_auto_run_id);
	
		$("#auto_run_simulation").css("display", "inline");
		$("#pause_simulation").css("display", "none");
	});

	$("input[name='simulation_memmap_format']").change(function(){



			$("#memory_map_table_rows").html("");
			for(var i = 0; i < program_data['memory'].length; i = i + 16 ){
				memory_map_table_rows_current = $("#memory_map_table_rows").html()

				var k = 0;
				memory_cell = [];
				for( var j=i; j<i+16; j=j+4){

					memory_cell[i+k] = program_data['memory'][j+3] +
										program_data['memory'][j+2] + 
										program_data['memory'][j+1] + 
										program_data['memory'][j];

					k = k + 1;
				}
				
				if( $("input[name=simulation_memmap_format]:checked").attr("id") == "simulation_memmap_format_hex"  ){
					$("#memory_map_table_rows").html(memory_map_table_rows_current
						+"<tr>"
							+"<td id=\"mem_pos_"+i+"_title\"><b>0x"+convert_data(i,16,8,"0")+"</b></td>"
							+"<td id=\"mem_pos_"+i+12+"\" contenteditable>0x"+ convert_data( parseInt(memory_cell[i+3],2),16,8,"0") +"</td>"
							+"<td id=\"mem_pos_"+i+8+"\" contenteditable>0x"+ convert_data( parseInt(memory_cell[i+2],2),16,8,"0") +"</td>"
							+"<td id=\"mem_pos_"+i+4+"\" contenteditable>0x"+ convert_data( parseInt(memory_cell[i+1],2),16,8,"0") +"</td>"
							+"<td id=\"mem_pos_"+i+"\" contenteditable>0x"+ convert_data( parseInt(memory_cell[i],2),16,8,"0") +"</td>"
						+"</tr>");
        	
				}else if(  $("input[name=simulation_memmap_format]:checked").attr("id") == "simulation_memmap_format_dec"  ){
					$("#memory_map_table_rows").html(memory_map_table_rows_current
						+"<tr>"
							+"<td id=\"mem_pos_"+i+"_title\"><b>0x"+convert_data(i,16,8,"0")+"</b></td>"
							+"<td id=\"mem_pos_"+i+12+"\" contenteditable>"+ bin2signed(memory_cell[i+3]) +"</td>"
							+"<td id=\"mem_pos_"+i+8+"\" contenteditable>"+  bin2signed(memory_cell[i+2]) +"</td>"
							+"<td id=\"mem_pos_"+i+4+"\" contenteditable>"+  bin2signed(memory_cell[i+1]) +"</td>"
							+"<td id=\"mem_pos_"+i+"\" contenteditable>"+  bin2signed(memory_cell[i]) +"</td>"
						+"</tr>");
				}

        	}
	});

	$("input[name='simulation_registers_format']").change(function(){
		if(  $("input[name=simulation_registers_format]:checked").attr("id") == "simulation_registers_format_hex"  ){
        	for( i=0; i<32; i++){
        		register_number = i.toString(2)
        		if(register_number.length<5){
        			pad = 5 - register_number.length;
        			register_number = "0".repeat(pad)+register_number;
        		}
        		//$("#reg_x"+i+"_val").html("0x"+simulator_response['registers'][register_number]);
        		$("#reg_x"+i+"_val").html("0x"+convert_data(parseInt(program_data['registers'][register_number], 2), 16,8,"0") );
        		//console.log("0x"+convert_data(parseInt(program_data['registers'][register_number], 2), 16,8,"0") );
        		//console.log(program_data['registers'][register_number]);
        	}
        	
		}else if(  $("input[name=simulation_registers_format]:checked").attr("id") == "simulation_registers_format_dec"  ){
        	for( i=0; i<32; i++){
        		register_number = i.toString(2)
        		if(register_number.length<5){
        			pad = 5 - register_number.length;
        			register_number = "0".repeat(pad)+register_number;
        		}
        		//$("#reg_x"+i+"_val").html("0x"+simulator_response['registers'][register_number]);
        		$("#reg_x"+i+"_val").html(bin2signed(program_data['registers'][register_number])) ;
        	
        			
        	}

		}
	});

	$("input[name=format_input_radio]").change(function(){

		  	$("#code").html("")
		  	$("#errors").html("")
		  	$("#memory").html("")
			data_format = this.value
			//console.log(data_format)
			//console.log(memory)
			//console.log(code)

			display_data("code", code[data_format], data_format);
	    	display_data("memory", memory[data_format], data_format);
	    	display_data("errors", errors,data_format);

	});

});

