from utils import settings, instructions, utilities
from simulator import simulator

'''
	TODOs: 
		configs.py
			terminar a tabela de instrucoes alguns tipo I

		simulator.py
			terminar decode:
			terminar execute: todas as instruções

'''

'''
ADDI $3, $0, 8		000000001000 00000 000 00011 0010011   
ADDI $4, $0, -2		111111111110 00000 000 00100 0010011   
ADD $5, $3, $4		0000000 00011 00100 000 00101 0110011  
ADDI $6, $0, 11 	000000001011 00000 000 00110 0010011   
XORI $7, $6, 25		000000010101 00110 100 00111 0010011
ORI $8, $6, 9		000000001001 00110 110 01000 0010011  
ANDI $9, $6, 19		000000010011 00110 111 01001 0010011
'''
def main():
	program_code='''00000000100000000000000110010011
11111111111000000000001000010011
00000000010000011000001010110011
00000000101100000000001100010011   
00000001010100110100001110010011
00000000100100110110010000010011  
00000001001100110111010010010011'''

	simulator.run(program_code)

	utilities.display_registers(-1,'bin')
	#settings.display_memory(0,100)


if __name__ == "__main__":
    main()