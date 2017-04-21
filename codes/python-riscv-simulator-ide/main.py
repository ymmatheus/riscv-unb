from utils import configs
from simulator import simulator

'''
	TODOs: 
		configs.py
			terminar a tabela de instrucoes alguns tipo I

		simulator.py
			terminar decode:
			terminar execute: todas as instruções

'''


def main():
	program_code='''010000000001000010000000110110011'''
	simulator.run(program_code)
	print(configs.instruction_table["0110011"]["type"])
	print(configs.instruction_table["0110011"]["000"]["0100000"])

if __name__ == "__main__":
    main()