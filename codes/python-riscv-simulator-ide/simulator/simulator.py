'''
	This module implements the simulation of a RISC-V ISA code
'''

from utils import configs

def fetch(code):
    ri=CODE_MEMORY[pc/4];
    pc+=4;
    return ri

def decode(instruction):

	# opcode
	# funct3
	# funct7
	# shamnt
	# imm12
	# rd
	# rs1
	# rs2

	if (instruction_table[opcode]["type"] == "r"):
		instruction_name = instruction_table[opdcode][funct3][funct7]
	elif (instruction_table[opcode]["type"] == "i"):
		if (instruction_table[opdcode][funct3] != "000"):
			instruction_name = instruction_table[opdcode][funct3]
		else:
			instruction_name = instruction_table[opdcode][funct3][imm12]

	elif (instruction_table[opcode]["type"] == "u"):
		instruction_name = instruction_table[opdcode]["inst_name"]
	elif (instruction_table[opcode]["type"] == "uj"):
		instruction_name = instruction_table[opdcode]["inst_name"]
	elif (instruction_table[opcode]["type"] == "s"):
		instruction_name = instruction_table[opdcode][funct3]
	elif (instruction_table[opcode]["type"] == "sb"):
		instruction_name = instruction_table[opdcode][funct3]

	return instruction_name

def execute(instruction_name):
	pass

def step(step_n=1):
	pass

def run(code):
	for i in code.split("\n"):
		print(i)

		