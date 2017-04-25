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
000000001000 00000 000 00011 0010011 ADDI $3, $0, 8
000000000010 00000 000 00100 0010011 ADDI $4, $0, -2
0000000 00011 00100 000 00101 0110011 ADD $5, $3, $4
'''
def main():
	program_code='''00000000100000000000000110010011\n11111111111000000000001000010011\n00000000010000011000001010110011'''
	simulator.run(program_code)

	utilities.display_registers()
	#settings.display_memory(0,100)


if __name__ == "__main__":
    main()