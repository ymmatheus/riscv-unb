from utils import settings, utilities
# All instructions from RV32G ISA
instruction_table = {

	# ADD, SUB, SLL, SRL, SRA, SLT, SLTU, XOR, AND, OR
	"0110011" : 
	{
		"type": "r",		
		# funct3
		"000" : 
		{	
			#funct7
			"0000000" : "add",
			"0100000" : "sub"
		},
		"001" :
		{
			"0000000" : "sll"
		},
		"010" :
		{
			"0000000" : "slt"
		},
		"011" :
		{
			"0000000" : "sltu"	
		},
		"100":
		{
			
			"0000000" : "xor"
		},
		"101":
		{	
			"0000000" : "srl",
			"0100000" : "sra"
		},
		"110":
		{
			"0000000" : "or"
		},
		"111":
		{
			"0000000" : "and"
		}
	},

	# JALR
	"1100111" : 
	{
		"type": "i",
		"000" : "jalr"
	},

	# ADDI, SLTI, SLTIU XORI ORI ANDI SLLI SRLI SRAI
	"0010011" : 
	{
		"type": "i",
		"000": "addi",
		"010": "slti",
		"011": "sltiu",
		"100": "xori",
		"110": "ori",
		"111": "andi",
		"001": 
		{
			"0000000": "slli"
		},
		"101": 
		{
			"0000000": "srli",
			"0100000": "srai"
		}
	},

	# FENCE, FENCE.I
	"0001111" : 
	{
		"type": "i",
		#### 

	},

	# ECALL EBREAK CSRRW CSRRS CSRRC CSRRWI CSRRSI CSRRCI
	"1110011" : 
	{
		"type": "i",
		#funct3
		"000": 
		{
			#"rd": "00000",
			#"rs1": "00000",
			#imm12
			"000000000000" : "ecall"
		},
		#funct3
		"000":
		{
			#"rd": "00000",
			#"rs1": "00000",
			#imm12
			"000000000001" : "ebreak"
		},
		"001": "csrrw",
		"010": "csrrs",
		"011": "csrrc",
		"101": "csrrwi",
		"110": "csrrsi",
		"111": "csrrci"
	},
	
	# LB LH LW LBU LHU
	"0000011" : 
	{
		"type": "i",
		# funct3
		"000": "lb",
		"001": "lh",
		"010": "lw",
		"100": "lbu",
		"101": "lhu"

	},
	
	# LUI
	"0110111" : 
	{ 
		"type": "u",
		"inst_name" : "lui"

	},

	# AUIPC
	"0010111" : 
	{ 
		"type": "u",
		"inst_name" : "auipc"
	}, 

	# JAL
	"1101111" : 
	{
		"type": "uj",	
		"inst_name" : "jal"
	},

	# SB SH SW 
	"0100011" : 
	{
		"type": "s",
		#funct3
		"000": "sb",
		"001": "sh",
		"010": "sw"
	},

	# BEQ BNE BLT BGE BLTU BGEU
	"1100011" : 
	{
		"type": "sb",
		#funct3
		"000" : "beq"  ,
		"001" : "bne"  ,
		"100" : "blt"  ,
		"101" : "bge"  ,
		"110" : "bltu" ,
		"111" : "bgeu"
	} 
}



def instr_lui():
	pass

def instr_auipc():
	pass

def instr_jal():
	pass

def instr_jalr():
	pass

def instr_beq():
	pass

def instr_bne():
	pass

def instr_blt():
	pass

def instr_bge():
	pass

def instr_bltu():
	pass

def instr_bgeu():
	pass

def instr_lb():
	pass

def instr_lh():
	pass

def instr_lw():
	pass

def instr_lbu():
	pass

def instr_lhu():
	pass

def instr_sb():
	pass

def instr_sh():
	pass

def instr_sw():
	pass

def instr_addi():
	'''ADDI adds the sign-extended 12-bit immediate to register rs1. Arithmetic overflow is ignored and
		the result is simply the low XLEN bits of the result. ADDI rd, rs1, 0 is used to implement the MV
		rd, rs1 assembler pseudo-instruction.'''
	
	#print(settings.registers[settings.rd])
	#print(settings.rd)
	#print(settings.bin2s(settings.imm_i[-12:]) )
	aux = utilities.bin2s(settings.registers[settings.rs1]) + utilities.bin2s(settings.imm_i)
	settings.registers[settings.rd] = utilities.s2bin(aux,32)

def instr_slti():
	'''
		SLTI (set less than immediate) places the value 1 in register rd if register rs1 is less than the sign-
		extended immediate when both are treated as signed numbers, else 0 is written to rd. SLTIU is
		similar but compares the values as unsigned numbers (i.e., the immediate is first sign-extended to
		XLEN bits then treated as an unsigned number). Note, SLTIU rd, rs1, 1 sets rd to 1 if rs1 equals
		zero, otherwise sets rd to 0 (assembler pseudo-op SEQZ rd, rs).
	'''
	if utilities.bin2s( settings.registers[settings.rs1] )  < utilities.bin2s( settings.imm_i) :
		settings.registers[settings.rd] = '1'.zfill(32)
	else:
		settings.registers[settings.rd] = '0'.zfill(32)


def instr_sltiu():
	if utilities.bin2u( settings.registers[settings.rs1] )  < utilities.bin2u( settings.imm_i) :
		settings.registers[settings.rd] = '1'.zfill(32)
	else:
		settings.registers[settings.rd] = '0'.zfill(32)

def instr_xori():
	'''
		ANDI, ORI, XORI are logical operations that perform bitwise AND, OR, and XOR on register rs1
		and the sign-extended 12-bit immediate and place the result in rd. Note, XORI rd, rs1, -1 performs
		a bitwise logical inversion of register rs1 (assembler pseudo-instruction NOT rd, rs).
	'''
	aux = ['0' for i in range(0,32)]
	for i in range(0,32):
		if((settings.registers[settings.rs1][i] == '1' and settings.imm_i[i] == '0') or (settings.registers[settings.rs1][i] == '0' and settings.imm_i[i] == '1')):
			aux[i] = '1'
		else:
			aux[i] = '0'
	settings.registers[settings.rd] = ''.join(aux)	

def instr_ori():
	aux = ['0' for i in range(0,32)]
	for i in range(0,32):
		if(settings.registers[settings.rs1][i] == '1' or settings.imm_i[i] == '1'):
			aux[i] = '1'
		else:
			aux[i] = '0'

	settings.registers[settings.rd] = ''.join(aux)	

def instr_andi():
	aux = ['0' for i in range(0,32)]
	for i in range(0,32):
		if(settings.registers[settings.rs1][i] == '1' and settings.imm_i[i] == '1'):
			aux[i] = '1'
		else:
			aux[i] = '0'

	settings.registers[settings.rd] = ''.join(aux)	

def instr_slli():
	pass

def instr_srli():
	pass

def instr_srai():
	pass

def instr_add():
	
	settings.registers[settings.rd] = utilities.s2bin(utilities.bin2s(settings.registers[settings.rs1]) + utilities.bin2s(settings.registers[settings.rs2]),32)


def instr_sub():
	settings.registers[settings.rd] = utilities.s2bin(utilities.bin2s(settings.registers[settings.rs1]) - utilities.bin2s(settings.registers[settings.rs2]),32)

def instr_sll():
	'''
	SLL, SRL, and SRA perform logical left, logical right, and arithmetic right shifts on the value in
	register rs1 by the shift amount held in the lower 5 bits of register rs2.
	'''
	shmnt = utilities.bin2u( settings.registers[settings.rs2][-5:] )
	print( settings.registers[settings.rs1] )
	settings.registers[settings.rd] = settings.registers[settings.rs1][shmnt:32] + ''.zfill(  shmnt  )
		
def instr_slt():
	if utilities.bin2s( settings.registers[settings.rs1] )  < utilities.bin2s( settings.registers[settings.rs2] ) :
		settings.registers[settings.rd] = '1'.zfill(32)
	else:
		settings.registers[settings.rd] = '0'.zfill(32)

def instr_sltu():
	if utilities.bin2u( settings.registers[settings.rs1] )  < utilities.bin2u( settings.registers[settings.rs2] ) :
		settings.registers[settings.rd] = '1'.zfill(32)
	else:
		settings.registers[settings.rd] = '0'.zfill(32)

def instr_xor():
	aux = ['0' for i in range(0,32)]
	for i in range(0,32):
		if((settings.registers[settings.rs1][i] == '1' and settings.registers[settings.rs2][i] == '0') or (settings.registers[settings.rs1][i] == '0' and settings.registers[settings.rs2][i] == '1')):
			aux[i] = '1'
		else:
			aux[i] = '0'
	settings.registers[settings.rd] = ''.join(aux)

def instr_srl():
	shmnt = utilities.bin2u( settings.registers[settings.rs2][-5:] )
	settings.registers[settings.rd] = ''.zfill( shmnt ) + settings.registers[settings.rs1][0:32-shmnt]

def instr_sra():
	shmnt = utilities.bin2u( settings.registers[settings.rs2][-5:] )
	if settings.registers[settings.rs1][0] == '0' :
		settings.registers[settings.rd] = ''.zfill( shmnt ) + settings.registers[settings.rs1][0:32-shmnt]
	else:
		shval = ''.join(['1' for i in range(0,shmnt)])
		settings.registers[settings.rd] = shval + settings.registers[settings.rs1][0:32-shmnt]


def instr_or():
	aux = ['0' for i in range(0,32)]
	for i in range(0,32):
		if(settings.registers[settings.rs1][i] == '1' or settings.registers[settings.rs2][i] == '1'):
			aux[i] = '1'
		else:
			aux[i] = '0'

	settings.registers[settings.rd] = ''.join(aux)	

def instr_and():
	aux = ['0' for i in range(0,32)]
	for i in range(0,32):
		if(settings.registers[settings.rs1][i] == '1' and settings.registers[settings.rs2][i] == '1'):
			aux[i] = '1'
		else:
			aux[i] = '0'

	settings.registers[settings.rd] = ''.join(aux)

def instr_fence():
	pass

def instr_fencei():
	pass

def instr_ecall():
	pass

def instr_ebreak():
	pass

def instr_csrrw():
	pass

def instr_csrrs():
	pass

def instr_csrrc():
	pass

def instr_csrrwi():
	pass

def instr_csrrsi():
	pass

def instr_csrrci():
	pass


instruction_execution_table = {
	"lui" : instr_lui,
	"auipc" : instr_auipc,
	"jal" : instr_jal,
	"jalr" : instr_jalr,
	"beq" : instr_beq,
	"bne" : instr_bne,
	"blt" : instr_blt,
	"bge" : instr_bge,
	"bltu" : instr_bltu,
	"bgeu" : instr_bgeu,
	"lb" : instr_lb,
	"lh" : instr_lh,
	"lw" : instr_lw,
	"lbu" : instr_lbu,
	"lhu" : instr_lhu,
	"sb" : instr_sb,
	"sh" : instr_sh,
	"sw" : instr_sw,
	"addi" : instr_addi,
	"slti" : instr_slti,
	"sltiu" : instr_sltiu,
	"xori" : instr_xori,
	"ori" : instr_ori,
	"andi" : instr_andi,
	"slli" : instr_slli,
	"srli" : instr_srli,
	"srai" : instr_srai,
	"add" : instr_add,
	"sub" : instr_sub,
	"sll" : instr_sll,
	"slt" : instr_slt,
	"sltu" : instr_sltu,
	"xor" : instr_xor,
	"srl" : instr_srl,
	"sra" : instr_sra,
	"or" : instr_or,
	"and" : instr_and,
	"fence" : instr_fence,
	"fencei" : instr_fencei,
	"ecall" : instr_ecall,
	"ebreak" : instr_ebreak,
	"csrrw" : instr_csrrw,
	"csrrs" : instr_csrrs,
	"csrrc" : instr_csrrc,
	"csrrwi" : instr_csrrwi,
	"csrrsi" : instr_csrrsi,
	"csrrci" : instr_csrrci
}
