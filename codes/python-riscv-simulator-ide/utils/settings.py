'''
	
	Variáveis

'''

# Decode variables
opcode = ''
rd = ''
funct3 = ''
rs1 = ''
rs2 = ''
funct7 = ''
imm_i = ''
imm_s = ''
imm_b = ''
imm_u = ''
imm_j = ''
shamnt = ''

# Architectural values
CODE_MEMORY_SIZE = 8192
DATA_MEMORY_SIZE = 8192
XLEN = 32

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
code_memory		= [0 for i in range(CODE_MEMORY_SIZE)]