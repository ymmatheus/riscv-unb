
DIRECTIVES_TABLE = [ ".data" , ".tet" , ".space" , ".word" , ".ascii" , ".asciiz", ".byte" ]

SYMBOL_TABLE = {}


REGISTER_NAMES = {
    "x0":"00000",
    "x1":"00001",
    "x2":"00010",
    "x3":"00011",
    "x4":"00100",
    "x5":"00101",
    "x6":"00110",
    "x7":"00111",
    "x8":"01000",
    "x9":"01001",
    "x10":"01010",
    "x11":"01011",
    "x12":"01100",
    "x13":"01101",
    "x14":"01110",
    "x15":"01111",
    "x16":"10000",
    "x17":"10001",
    "x18":"10010",
    "x19":"10011",
    "x20":"10100",
    "x21":"10101",
    "x22":"10110",
    "x23":"10111",
    "x24":"11000",
    "x25":"11001",
    "x26":"11010",
    "x27":"11011",
    "x28":"11100",
    "x29":"11101",
    "x30":"11110",
    "x31":"11111",
    "zero":"00000",
    "ra":"00001",
    "sp":"00010",
    "gp":"00011",
    "tp":"00100",
    "t0":"00101",
    "t1":"00110",
    "t2":"00111",
    "fp":"01000",
    "s0":"01000",
    "s1":"01001",
    "a0":"01010",
    "a1":"01011",
    "a2":"01100",
    "a3":"01101",
    "a4":"01110",
    "a5":"01111",
    "a6":"10000",
    "a7":"10001",
    "s2":"10010",
    "s3":"10011",
    "s4":"10100",
    "s5":"10101",
    "s6":"10110",
    "s7":"10111",
    "s8":"11000",
    "s9":"11001",
    "s10":"11010",
    "s11":"11011",
    "t3":"11100",
    "t4":"11101",
    "t5":"11110",
    "t6":"11111" 
}


INSTRUCTION_TABLE = {
    "lui" : {
        "size":4,
        "opcode":"0110111"
        },
    "auipc" : {
        "size":4,
        "opcode":"0010111"
        },
    "jal" : {
        "size":4,
        "opcode":0,
        "funct3":0,
        "funct7":0
        },
    "jalr" : {
        "size":4,
        "opcode":"1100111",
        "funct3":0,
        "funct7":0
        },
    "beq" : {
        "size":4,
        "opcode":0,
        "funct3":0,
        "funct7":0
        },
    "bne" : {
        "size":4,
        "opcode":0,
        "funct3":0,
        "funct7":0
        },
    "blt" : {
        "size":4,
        "opcode":0,
        "funct3":0,
        "funct7":0
        },
    "bge" : {
        "size":4,
        "opcode":0,
        "funct3":0,
        "funct7":0
        },
    "bltu" : {
        "size":4,
        "opcode":0,
        "funct3":0,
        "funct7":0
        },
    "bgeu" : {
        "size":4,
        "opcode":0,
        "funct3":0,
        "funct7":0
        },
    "lb" : {
        "size":4,
        "opcode":0,
        "funct3":0,
        "funct7":0
        },
    "lh" : {
        "size":4,
        "opcode":0,
        "funct3":0,
        "funct7":0
        },
    "lw" : {
        "size":4,
        "opcode":0,
        "funct3":0,
        "funct7":0
        },
    "lbu" : {
        "size":4,
        "opcode":0,
        "funct3":0,
        "funct7":0
        },
    "lhu" : {
        "size":4,
        "opcode":0,
        "funct3":0,
        "funct7":0
        },
    "sb" : {
        "size":4,
        "opcode":0,
        "funct3":0,
        "funct7":0
        },
    "sh" : {
        "size":4,
        "opcode":0,
        "funct3":0,
        "funct7":0
        },
    "sw" : {
        "size":4,
        "opcode":0,
        "funct3":0,
        "funct7":0
        },
    "addi" : {
        "size":4,
        "opcode":"0010011",
        "funct3":"000"
        },
    "slti" : {
        "size":4,
        "opcode":"0010011",
        "funct3":"010"
        },
    "sltiu" : {
        "size":4,
        "opcode":"0010011",
        "funct3":"011"
        },
    "xori" : {
        "size":4,
        "opcode":"0010011",
        "funct3":"100"
        },
    "ori" : {
        "size":4,
        "opcode":"0010011",
        "funct3":"110"
        },
    "andi" : {
        "size":4,
        "opcode":"0010011",
        "funct3":"111"
        },
    "slli" : {
        "size":4,
        "opcode":"0010011",
        "funct3":"001"
        },
    "sri" : {
        "size":4,
        "opcode":"0010011",
        "funct3":"101"
        },
    "add" : {
        "size":4,
        "opcode": "0110011",
        "funct3": "000",
        "funct7": "0000000"
        },
    "sub" : {
        "size":4,
        "opcode": "0110011",
        "funct3": "000",
        "funct7": "0100000"
        },
    "sll" : {
        "size":4,
        "opcode": "0110011",
        "funct3": "001",
        "funct7": "0000000"
        },
    "slt" : {
        "size":4,
        "opcode": "0110011",
        "funct3": "010",
        "funct7": "0000000"
        },
    "sltu" : {
        "size":4,
        "opcode": "0110011",
        "funct3": "011",
        "funct7": "0000000"
        },
    "xor" : {
        "size":4,
        "opcode": "0110011",
        "funct3": "100",
        "funct7": "0000000"
        },
    "srl" : {
        "size":4,
        "opcode": "0110011",
        "funct3": "101",
        "funct7": "0000000"
        },
    "sra" : {
        "size":4,
        "opcode": "0110011",
        "funct3": "101",
        "funct7": "0100000"
        },
    "or" : {
        "size":4,
        "opcode": "0110011",
        "funct3": "110",
        "funct7": "0000000"
        },
    "and" : {
        "size":4,
        "opcode": "0110011",
        "funct3": "111",
        "funct7": "0000000"
        },
    "fence" : {
        "size":4,
        "opcode":0,
        "funct3":0,
        "funct7":0
        },
    "fencei" : {
        "size":4,
        "opcode":0,
        "funct3":0,
        "funct7":0
        },
    "env" : {
        "size":4,
        "opcode":0,
        "funct3":0,
        "funct7":0
        },
    "csrrw" : {
        "size":4,
        "opcode":0,
        "funct3":0,
        "funct7":0
        },
    "csrrs" : {
        "size":4,
        "opcode":0,
        "funct3":0,
        "funct7":0
        },
    "csrrc" : {
        "size":4,
        "opcode":0,
        "funct3":0,
        "funct7":0
        },
    "csrrwi" : {
        "size":4,
        "opcode":0,
        "funct3":0,
        "funct7":0
        },
    "csrrsi" : {
        "size":4,
        "opcode":0,
        "funct3":0,
        "funct7":0
        },
    "csrrci" : {
        "size":4,
        "opcode":0,
        "funct3":0,
        "funct7":0
        },
}

''' Funcao pega uma linha e checa erros de sintaxe, e retorna um dicionario com label, operacao e operandos '''
def split_tokens(line, line_number):
    
    label = ""
    operation = ""
    operands = ""

    # remove comments
    if ";" in line:     
        line = line.split(";")[0]
    
    # check if line is empty
    if line != "":
        # get label
        if ":" in line:
            tokens = line.split(":")
            tokens_size = len(tokens)
            # check more than one label
            # print(tokens_size)
            if tokens_size > 2 :
                print("Syntax Error: More than one label in the same line. Line: " + str(line_number))
                return -1

            label = tokens[0]
            tokens_op = tokens[1]
        else:
            tokens_op = line

        operation, operands_raw = tokens_op.split(" ", 1)
        operands = operands_raw.split(",")

        # check if label is one word 
        if len(label.split(" ")) > 1 :
            print("Syntax Error: More than one word for label before symbol ':'. Line: " + str(line_number))
            return -1

        # remove empty spaces on operation
        operation = operation.replace(" ", "")

        # remove empty spaces of operands
        for i in range( len(operands) ):
            operands[i] = operands[i].replace(" ", "")


    return {"label":label, "operation":operation, "operands":operands }


def first_pass(code_tet):

    contador_pos = 0
    contador_linha = 1

    # To lower case
    code_tet = code_tet.lower()
    # Separa por linhas
    code_tet = code_tet.split("\n")


    code_tet_aux = list()
    for line in code_tet: # para cada linha de codigo
        
        # remoe os espacos do inicio e final
        line = line.strip()

        # ignora se for comentario ou linha vazia
        if(  line == ""  or  line[0]==";"):
            pass
        else:

            all_tokens = split_tokens(line, contador_linha)
            # se operacao e operandos nao for vazio
            if all_tokens["operation"] != "" or all_tokens["operands"] != "" :
                #print( "Contador linha:  "+str(contador_linha) + "   "+str(line))
                #print(all_tokens)
                #print("contador pos: "+str(contador_pos))
                #print("--")

                # se tiver label
                if all_tokens['label'] != '':
                    # procura label na tabela de simbolos
                    if all_tokens['label'] in SYMBOL_TABLE:
                        # simbolo redefinido
                        print("Error: Duplicated Symbol")
                        return 1
                    else:
                        # insere rotulo e contador_posicao na tablea de simbolos
                        SYMBOL_TABLE[ all_tokens['label'] ] = contador_pos;

                # procura operacao na tabela de instrucoes
                if all_tokens['operation'] in INSTRUCTION_TABLE:
                    #print("incrementa pos "+ str(INSTRUCTION_TABLE[all_tokens['operation']]['size']))
                    contador_pos = contador_pos + INSTRUCTION_TABLE[all_tokens['operation']]['size']
                else:
                    if all_tokens['operation'] in DIRECTIVES_TABLE:
                        pass
                        #DIRECTIVES_TABLE[all_tokens['operation']]
                        #contador_pos = x
                    else:
                        print("Error: Operation "+ str(all_tokens['operation']) + " not recognized. Line:"+str(contador_linha)  )
                        return 2
            contador_linha = contador_linha + 1
        

    return 0;

def second_pass(code_tet):
    #1
    contador_pos = 0
    contador_linha = 1

    # To lower case
    code_tet = code_tet.lower()
    # Separa por linhas
    code_tet = code_tet.split("\n")


    code_tet_aux = list()
    for line in code_tet: # para cada linha de codigo
        # remoe os espacos do inicio e final
        line = line.strip()

        # ignora se for comentario ou linha vazia
        if(line == "" or line[0]==";" ):
            pass
        else:

            all_tokens = split_tokens(line, contador_linha)

#    2   -   Para cada operando que e simbolo
#            Procura operando na TS
#            Se nao achou: 
#                Erro, simbolo indefinido

            print(line)
            for operand in all_tokens['operands']:
                print(operand)
                if( operand in REGISTER_NAMES):
                    print("Registrador!")
                else:
                    #print("Simbolo")
                    if operand in SYMBOL_TABLE:
                        print("Simbolo existente")
                    else:
                        #if symbol is number or address label:

                        #else simbolo indefinido


                        print("Simbolo inexistente")    
            print("\n")
    
#    3   -   Procura operacao na tabela de instrucoes
#            Se achou:
#                contador_posicao = contador_posicao + tamanho da instrucao
#                Se numero e tipo dos operandos esta correto entao
#                    gera codigo objeto conforme formato da instrucao
#                Senao: 
#                    Erro, operando invalido



    
#    4   -   Senao:
#                Procura operacao na tabela de diretivas
#                Se achou:
#                    Chama subrotina que executa a diretiva
#                    Contador_posicao = valor retornado pela subrotina
#                Senao: 
#                    Erro, operacao nao identificada
#            Contador_linha = contador_linha + 1



            # procura operacao na taela de instrucoes
            if all_tokens['operation'] in INSTRUCTION_TABLE:
                #print(INSTRUCTION_TABLE[ all_tokens['operation'] ])
                contador_pos = contador_pos + INSTRUCTION_TABLE[ all_tokens['operation'] ]['size']
            else: # se nao tiver intrucao, procura em diretivas
                if all_tokens['operation'] in DIRECTIVES_TABLE: 
                    pass
                    #DIRECTIVES_TABLE[all_tokens['operation']]
                    #contador_pos = x
                else: # senao existe instrucao nem diretiva lanca erro
                    print("Error: Operation "+ str(all_tokens['operation']) + " not recognized. Line:"+str(contador_linha)  )
                    return 2
            contador_linha = contador_linha + 1


    return 0;






code = '''ADDI x1, zero, 56
ADDI t1, t0, 44
label1:ADDI t1, t0, 441
ADDI  t1 , t0, 442
;comentaario
label2:ADDI t1, t0,  443

label3:ADD t2, t1, t0

ADDI t1, t0, 44 ; comments
ADDI  t1 , t0, 444  

ADDI t1, t0, 445
ADDI t1, t0, 446 
ADDI t1, t0, 44'''

code2 = '''ADDI x1, zero, 56
ADDI t1, t0, 44
label1:ADDI t1, t0, 441
ADDI  t1 , t0, 442
;comentaario
label2:ADDI t1, t0,  443

label3:ADD t2, t1, t0

ADDI t1, t0, 44 ; comments
ADDI  t1 , t0, 444  

ADDI t1, t0, 445
ADDI t1, t0, 446 
ADDI t1, t0, 44'''

code3 = '''ADDI x1, zero, 56
ADD t1, t0, zero
label1:ADDI t1, t0, 441
ADDI  t1 , t0, 442

label2:ADDI t1, t0,  443'''


#print(code)
#print("\n")

print("Primeira Passsagem\n")
fp_ret = first_pass(code3)
print("\n")
if fp_ret == 0 :
    pass
    #print(SYMBOL_TABLE)
    print("Segunda Passsagem\n")
    sp_ret = second_pass(code3)

#print(scanner(processed_code))
