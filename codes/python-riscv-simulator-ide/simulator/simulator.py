'''
	This module implements the simulation of a RISC-V ISA code
'''

'''
	todo: misaligned memory load store
	add the decode variables on config file for global
'''

from utils import settings, instructions, utilities

def fetch(pc):
	#print("FETCHING")
	ri=settings.code_memory[pc//4];
	settings.pc = pc + 4;
	#print(ri)
	return ri

def decode(instruction):
	#print("DECODING")
	# decoding type R
	settings.opcode = instruction[25:32]
	settings.rd = instruction[20:25]
	settings.funct3 = instruction[17:20]
	settings.rs1 = instruction[12:17]
	settings.rs2 = instruction[7:12]
	settings.funct7 = instruction[0:7]

	# immediates
	settings.imm_i = instruction[0]*21 + instruction[1:7] + instruction[7:11] + instruction[11] 
	settings.imm_s = instruction[0]*21 + instruction[1:7] + instruction[20:24] + instruction[24]
	settings.imm_b = instruction[0]*20 + instruction[24] + instruction[1:7] + instruction[20:24] + "0"
	#print("!!!!!!")
	#print( utilities.bin2s( settings.imm_b  ) )
	#print( utilities.bin2s( instruction ) )
	#print("!!!!!!!")
	settings.imm_u = instruction[0] + instruction[1:12] + instruction[12:20] + "0"*12 
	settings.imm_j = instruction[0]*12 + instruction[12:20] + instruction[11] + instruction[1:7] + instruction[7:11] + "0"

	#shift ammount
	#print(instructions.instruction_table[settings.opcode]["type"])
	settings.shamnt = settings.rs2
	if settings.opcode in instructions.instruction_table.keys():
		if (instructions.instruction_table[settings.opcode]["type"] == "r"):
		
			instruction_name = instructions.instruction_table[settings.opcode][settings.funct3][settings.funct7]
		
		elif (instructions.instruction_table[settings.opcode]["type"] == "i"):

			instruction_name = instructions.instruction_table[settings.opcode][settings.funct3]
		
		elif (instructions.instruction_table[settings.opcode]["type"] == "u"):
		
			instruction_name = instructions.instruction_table[settings.opcode]["inst_name"]
		
		elif (instructions.instruction_table[settings.opcode]["type"] == "uj"):
		
			instruction_name = instructions.instruction_table[settings.opcode]["inst_name"]
		
		elif (instructions.instruction_table[settings.opcode]["type"] == "s"):
		
			instruction_name = instructions.instruction_table[settings.opcode][settings.funct3]
		
		elif (instructions.instruction_table[settings.opcode]["type"] == "sb"):
		
			instruction_name = instructions.instruction_table[settings.opcode][settings.funct3]

		elif settings.opcode == '0000000':

			instruction_name = "nop"

		else:

			instruction_name = "unknown"


	else:

		instruction_name = "unknown"

	#print(instruction_name)
	return instruction_name

def execute(instruction_name):
	#print("EXECUTING")
	#print(instruction_name)
	#print(instructions.instruction_execution_table[instruction_name])
	func_driver = instructions.instruction_execution_table[instruction_name]
	#print(instruction_name)
	#print()
	# hard wired zero
	settings.registers['00000'] = "00000000000000000000000000000000"
	func_driver()	

def run( code, memory, registers, pc, console_input, step_count=-1):

	# Load text program to code memory
	i=0	
	for inst in code:
		settings.code_memory[i] = inst		
		i=i+1

	#settings.code_memory[i-1] = 'exit'
	#print(settings.code_memory)

	# Load program data to data memory
	i=0
	for data in memory:		
		settings.data_memory[i] = data
		i=i+1
		
	# Load register data
	for i in range(32):
		settings.registers[utilities.u2bin(i,5)] = registers[utilities.u2bin(i,5)]
	#while(settings.code_memory[settings.pc//4]):
	it=0
	settings.pc = pc
	while(settings.pc//4 < 20 and it<1000000 and step_count != 0 and settings.exit_flag == False):
	#while(settings.pc//4 < 20):
		#print(settings.pc)
		#print(settings.registers['00101'])
		execute(decode(fetch(settings.pc)))
		it = it + 1 # avoid infinite loop
		step_count = step_count - 1
		
	#print(settings.registers)

	# copy data
	pc_aux  			= settings.pc
	console_output_aux 	= settings.console_output.copy()
	reg_aux  			= settings.registers.copy()
	data_mem_aux  		= settings.data_memory.copy()


	# reset variables
	settings.exit_flag			= False
	settings.console_input 		= []
	settings.console_output 	= []
	settings.pc 				= 0
	settings.data_memory        = ['00000000' for i in range(settings.DATA_MEMORY_SIZE)] # each address is a byte
	settings.code_memory        = [settings.XLEN*'0' for i in range(settings.CODE_MEMORY_SIZE)]
	for i in range(32):
		settings.registers[utilities.u2bin(i,5)] = '00000000000000000000000000000000'	


	return {"registers": reg_aux, "memory_map":data_mem_aux, "program_counter":pc_aux,"console_output":console_output_aux}

