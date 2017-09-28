from utils import settings, instructions, utilities
from simulator import simulator
from assembler import assembler
'''
	TODOs:
		instructions.py
			- terminar execute: todas as instruções
			- alinhamento instrucoes
        - Gerar código objeto em HEX e MIF
'''

def main():
    code = '''ADDI x1, zero, 56
    ADDI t1, t0, 44
    label1:ADDI t1, t0, 441
    ADDI  t1 , t0, 442
    #comentaario
    label2:ADDI t1, t0,  443

    label3:ADD t2, t1, t0

    ADDI t1, t0, 44 # comments
    ADDI  t1 , t0, 444  

    ADDI t1, t0, 445
    ADDI t1, t0, 446 
    ADDI t1, t0, 44'''

    code2 = '''ADDI x1, zero, 56
    ADDI t1, t0, 44
    label1:ADDI t1, t0, 441
    ADDI  t1 , t0, 442
    #comentaario
    label2:ADDI t1, t0,  443

    label3:ADD t2, t1, t0

    ADDI t1, t0, 44 # comments
    ADDI  t1 , t0, 444  

    ADDI t1, t0, 445
    ADDI t1, t0, 446 
    ADDI t1, t0, 44'''

    code3 = '''ADDI x1, zero, 56
    ADD t1, t0, zero
    label1:ADDI t1, t0, 16
    ADDI  t1 , t0, -3  # comentando
    # comentando
    ADDI  t1 , x6, 32

    LuI  t1,-999

    label2:ADDI t1, t0, -766'''

    cod_obj = assembler.assemble(code3)

    utilities.display_codeobj(cod_obj,"hex")
    utilities.save_to_file(cod_obj,"mif")

# 	program_code='''00000000100000000000000110010011
# 11111111111000000000001000010011
# 00000000010000011000001010110011
# 00000000101100000000001100010011   
# 00000001010100110100001110010011
# 00000000100100110110010000010011  
# 00000001001100110111010010010011'''


	#simulator.run(program_code)

	#utilities.display_registers(-1, 'hex')
	#settings.display_memory(0, 100, 'hex')

if __name__ == "__main__":
    main()
