'''
Instruction opcode funct3 funct7
LUI 0110111
AUIPC 0010111
JAL 1101111
JALR 1100111 000
BEQ 1100011 000
BNE 1100011 001
BLT 1100011 100
BGE 1100011 101
BLTU 1100011 110
BGEU 1100011 111
LB 0000011 000
LH 0000011 001
LW 0000011 010
LBU 0000011 100
LHU 0000011 101
SB 0100011 000
SH 0100011 001
SW 0100011 010
ADDI 0010011 000
SLTI 0010011 010
SLTIU 0010011 011
XORI 0010011 100
ORI 0010011 110
ANDI 0010011 111
SLLI 0010011 001 0000000
SRLI 0010011 101 0000000
SRAI 0010011 101 0100000
ADD 0110011 000 0000000
SUB 0110011 000 0100000
SLL 0110011 001 0000000
SLT 0110011 010 0000000
SLTU 0110011 011 0000000
XOR 0110011 100 0000000
SRL 0110011 101 0000000
SRA 0110011 101 0100000
OR 0110011 110 0000000
AND 0110011 111 0000000
FENCE 0001111 000
FENCE.I 0001111 001
ECALL 1110011 000
EBREAK 1110011 000
CSRRW 1110011 001
CSRRS 1110011 010
CSRRC 1110011 011
CSRRWI 1110011 101
CSRRSI 1110011 110
CSRRCI 1110011 111

'''
'''
	
	Variáveis

'''


CODE_MEMORY_SIZE = 8192
DATA_MEMORY_SIZE = 8192
XLEN = 32

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
		}
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


registers 		= {	"00000":0, #0 $zero
					"00001":0, #1 $at
					"00010":0, #2  $v0
					"00011":0, #3  $v1
					"00100":0, #4  $a0
					"00101":0, #5  $a1
					"00110":0, #6  $a2		
					"00111":0, #7  $a3
					"01000":0, #8  $t0				
					"01001":0, #9  $t1
					"01010":0, #10 $t2
					"01011":0, #11 $t3
					"01100":0, #12 $t4
					"01101":0, #13 $t5
					"01110":0, #14 $t6
					"01111":0, #15 $t7
					"10000":0, #16 $s0
					"10001":0, #17 $s1
					"10010":0, #18 $s2
					"10011":0, #19 $s3
					"10100":0, #20 $s4
					"10101":0, #21 $s5
					"10110":0, #22 $s6
					"10111":0, #23 $s7
					"11000":0, #24 $t8
					"11001":0, #25 $t9
					"11010":0, #26 $k0
					"11011":0, #27 $k1
					"11100":0, #28 $gp
					"11101":0, #29 $sp
					"11110":0, #30 $fp
					"11111":0, #31 $ra					
				}

pc = 0				
ri = 0
data_memory		= [0 for i in range(DATA_MEMORY_SIZE)]
data_memory		= [0 for i in range(CODE_MEMORY_SIZE)]


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
	pass

def instr_slti():
	pass

def instr_sltiu():
	pass

def instr_xori():
	pass

def instr_ori():
	pass

def instr_andi():
	pass

def instr_slli():
	pass

def instr_srli():
	pass

def instr_srai():
	pass

def instr_add():
	pass

def instr_sub():
	pass

def instr_sll():
	pass

def instr_slt():
	pass

def instr_sltu():
	pass

def instr_xor():
	pass

def instr_srl():
	pass

def instr_sra():
	pass

def instr_or():
	pass

def instr_and():
	pass

def instr_fence():
	pass

def instr_fence():
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
	"fence" : instr_fence,
	"ecall" : instr_ecall,
	"ebreak" : instr_ebreak,
	"csrrw" : instr_csrrw,
	"csrrs" : instr_csrrs,
	"csrrc" : instr_csrrc,
	"csrrwi" : instr_csrrwi,
	"csrrsi" : instr_csrrsi,
	"csrrci" : instr_csrrci
}

def num2binstr(i):
	binstr = ""
	while(i>1):
		rmindr = i%2
		i = i//2
		binstr += str(rmindr)
		print(i)
	binstr += str(i)
	return(binstr[::-1])

def binstr2int(i):
	pass
	#int = 0
	#while(i>1):
	#	rmindr = i%2
	#	i = i//2
	#	binstr += str(rmindr)
	#	print(i)
	#binstr += str(i)
	#return(binstr[::-1])