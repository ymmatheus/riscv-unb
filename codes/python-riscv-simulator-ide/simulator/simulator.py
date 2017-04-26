'''
	This module implements the simulation of a RISC-V ISA code
'''

'''
	todo: misaligned memory load store
	add the decode variables on config file for global
'''

from utils import settings, instructions, utilities

def fetch(pc):
    ri=settings.code_memory[pc//4];
    settings.pc = pc + 4;
    #print(ri)
    return ri

def decode(instruction):

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
	settings.imm_u = instruction[0] + instruction[1:12] + instruction[12:20] + "0"*12 
	settings.imm_j = instruction[0]*12 + instruction[12:20] + instruction[11] + instruction[1:7] + instruction[7:11] + "0"

	#shift ammount
	settings.shamnt = settings.rs2

	if (instructions.instruction_table[settings.opcode]["type"] == "r"):
	
		instruction_name = instructions.instruction_table[settings.opcode][settings.funct3][settings.funct7]
	
	elif (instructions.instruction_table[settings.opcode]["type"] == "i"):
	
		if (instructions.instruction_table[settings.opcode][settings.funct3] != "000"):
			instruction_name = instructions.instruction_table[settings.opcode][settings.funct3]
		else:
			instruction_name = instructions.instruction_table[settings.opcode][settings.funct3][imm12]
	
	elif (instructions.instruction_table[settings.opcode]["type"] == "u"):
	
		instruction_name = instructions.instruction_table[settings.opcode]["inst_name"]
	
	elif (instructions.instruction_table[settings.opcode]["type"] == "uj"):
	
		instruction_name = instructions.instruction_table[settings.opcode]["inst_name"]
	
	elif (instructions.instruction_table[settings.opcode]["type"] == "s"):
	
		instruction_name = instructions.instruction_table[settings.opcode][settings.funct3]
	
	elif (instructions.instruction_table[settings.opcode]["type"] == "sb"):
	
		instruction_name = instructions.instruction_table[settings.opcode][settings.funct3]

	#print(instruction_name)
	return instruction_name

def execute(instruction_name):
	func_driver = instructions.instruction_execution_table[instruction_name]
	func_driver()

def step(step_n=1):
	pass
	

def run(code):

	# Load text program to code memory
	i=0
	for inst in code.split("\n"):
		settings.code_memory[i] = inst
		#print(i)
		i=i+1
	settings.code_memory[i] = 'exit'
	#print(settings.code_memory)

	while(settings.code_memory[settings.pc//4] != 'exit'):
		execute(decode(fetch(settings.pc)))

		