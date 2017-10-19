from utils import settings, instructions, utilities
from simulator import simulator
from assembler import assembler
'''
	TODOs:
		instructions.py
			- terminar execute: todas as instruções
			- alinhamento instrucoes

        GUI:
            - Layout geral
                - Menu
                    - Funcoes arquivos
                        - Abrir
                        - Salvar
                        - Novo ( Gerar já um boilerplate com section data section text)

                - Botoes simulacao
                    - Run
                    - Step
                    - Speed

                - Editor de texto
                    - Highlight
                    - Alterar tamanho da fonte
                    - Funcionamento dos Tabs

                - Register Map

                - Memory Map


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

    LuI  a1,0
    addi    a1,a1,8 # 8
    auipc   a1,0
    jalr x9,x11,label1
    jal x8, label2
    label2:ADDI t1, t0, -766'''

    cod_obj = assembler.assemble(code3)

    utilities.display_codeobj(cod_obj,"hex")
    utilities.save_to_file(cod_obj,"mif", r"fileout") 

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
