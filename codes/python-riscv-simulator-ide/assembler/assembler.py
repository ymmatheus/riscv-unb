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
        "type":"u",
        "size":4,
        "opcode":"0110111",
        "operands":[]
        },
    "auipc" : {
        "type":"u",
        "size":4,
        "opcode":"0010111",
        "operands":[]
        },
    "jal" : {
        "type":"uj",
        "size":4,
        "opcode":0,
        "funct3":0,
        "funct7":0,
        "operands":[]
        },
    "jalr" : {
        "type":"i",
        "size":4,
        "opcode":"1100111",
        "funct3":0,
        "funct7":0,
        "operands":[]
        },
    "beq" : {
        "type":"sb",
        "size":4,
        "opcode":0,
        "funct3":0,
        "funct7":0,
        "operands":[]
        },
    "bne" : {
        "type":"sb",
        "size":4,
        "opcode":0,
        "funct3":0,
        "funct7":0,
        "operands":[]
        },
    "blt" : {
        "type":"sb",
        "size":4,
        "opcode":0,
        "funct3":0,
        "funct7":0,
        "operands":[]
        },
    "bge" : {
        "type":"sb",
        "size":4,
        "opcode":0,
        "funct3":0,
        "funct7":0,
        "operands":[]
        },
    "bltu" : {
        "type":"sb",
        "size":4,
        "opcode":0,
        "funct3":0,
        "funct7":0,
        "operands":[]
        },
    "bgeu" : {
        "type":"sb",
        "size":4,
        "opcode":0,
        "funct3":0,
        "funct7":0,
        "operands":[]
        },
    "lb" : {
        "type":"i",
        "size":4,
        "opcode":0,
        "funct3":0,
        "funct7":0,
        "operands":[]
        },
    "lh" : {
        "type":"i",
        "size":4,
        "opcode":0,
        "funct3":0,
        "funct7":0,
        "operands":[]
        },
    "lw" : {
        "type":"i",
        "size":4,
        "opcode":0,
        "funct3":0,
        "funct7":0,
        "operands":[]
        },
    "lbu" : {
        "type":"i",
        "size":4,
        "opcode":0,
        "funct3":0,
        "funct7":0,
        "operands":[]
        },
    "lhu" : {
        "type":"i",
        "size":4,
        "opcode":0,
        "funct3":0,
        "funct7":0,
        "operands":[]
        },
    "sb" : {
        "type":"s",
        "size":4,
        "opcode":0,
        "funct3":0,
        "funct7":0,
        "operands":[]
        },
    "sh" : {
        "type":"s",
        "size":4,
        "opcode":0,
        "funct3":0,
        "funct7":0,
        "operands":[]
        },
    "sw" : {
        "type":"s",
        "size":4,
        "opcode":0,
        "funct3":0,
        "funct7":0,
        "operands":[]
        },
    "addi" : {
        "type":"i",
        "size":4,
        "opcode":"0010011",
        "funct3":"000",
        "operands":["register", "register", "number"]
        },
    "slti" : {
        "type":"i",
        "size":4,
        "opcode":"0010011",
        "funct3":"010",
        "operands":[]
        },
    "sltiu" : {
        "type":"i",
        "size":4,
        "opcode":"0010011",
        "funct3":"011",
        "operands":[]
        },
    "xori" : {
        "type":"i",
        "size":4,
        "opcode":"0010011",
        "funct3":"100",
        "operands":[]
        },
    "ori" : {
        "type":"i",
        "size":4,
        "opcode":"0010011",
        "funct3":"110",
        "operands":[]
        },
    "andi" : {
        "type":"i",
        "size":4,
        "opcode":"0010011",
        "funct3":"111",
        "operands":[]
        },
    "slli" : {
        "type":"i",
        "size":4,
        "opcode":"0010011",
        "funct3":"001",
        "operands":[]
        },
    "sri" : {
        "type":"i",
        "size":4,
        "opcode":"0010011",
        "funct3":"101",
        "operands":[]
        },
    "add" : {
        "type":"r",
        "size":4,
        "opcode": "0110011",
        "funct3": "000",
        "funct7": "0000000",
        "operands":["register","register","register"]
        },
    "sub" : {
        "type":"r",
        "size":4,
        "opcode": "0110011",
        "funct3": "000",
        "funct7": "0100000",
        "operands":["register","register","register"]
        },
    "sll" : {
        "type":"r",
        "size":4,
        "opcode": "0110011",
        "funct3": "001",
        "funct7": "0000000",
        "operands":["register","register","register"]
        },
    "slt" : {
        "type":"r",
        "size":4,
        "opcode": "0110011",
        "funct3": "010",
        "funct7": "0000000",
        "operands":["register","register","register"]
        },
    "sltu" : {
        "type":"r",
        "size":4,
        "opcode": "0110011",
        "funct3": "011",
        "funct7": "0000000",
        "operands":[]
        },
    "xor" : {
        "type":"r",
        "size":4,
        "opcode": "0110011",
        "funct3": "100",
        "funct7": "0000000",
        "operands":[]
        },
    "srl" : {
        "type":"r",
        "size":4,
        "opcode": "0110011",
        "funct3": "101",
        "funct7": "0000000",
        "operands":[]
        },
    "sra" : {
        "type":"r",
        "size":4,
        "opcode": "0110011",
        "funct3": "101",
        "funct7": "0100000",
        "operands":[]
        },
    "or" : {
        "type":"r",
        "size":4,
        "opcode": "0110011",
        "funct3": "110",
        "funct7": "0000000",
        "operands":[]
        },
    "and" : {
        "type":"r",
        "size":4,
        "opcode": "0110011",
        "funct3": "111",
        "funct7": "0000000",
        "operands":[]
        },
    "fence" : {
        "type":"i",
        "size":4,
        "opcode":0,
        "funct3":0,
        "funct7":0,
        "operands":[]
        },
    "fencei" : {
        "type":"i",
        "size":4,
        "opcode":0,
        "funct3":0,
        "funct7":0,
        "operands":[]
        },
    "env" : {
        "type":"i",
        "size":4,
        "opcode":0,
        "funct3":0,
        "funct7":0,
        "operands":[]
        },
    "csrrw" : {
        "type":"i",
        "size":4,
        "opcode":0,
        "funct3":0,
        "funct7":0,
        "operands":[]
        },
    "csrrs" : {
        "type":"i",
        "size":4,
        "opcode":0,
        "funct3":0,
        "funct7":0,
        "operands":[]
        },
    "csrrc" : {
        "type":"i",
        "size":4,
        "opcode":0,
        "funct3":0,
        "funct7":0,
        "operands":[]
        },
    "csrrwi" : {
        "type":"i",
        "size":4,
        "opcode":0,
        "funct3":0,
        "funct7":0,
        "operands":[]
        },
    "csrrsi" : {
        "type":"i",
        "size":4,
        "opcode":0,
        "funct3":0,
        "funct7":0,
        "operands":[]
        },
    "csrrci" : {
        "type":"i",
        "size":4,
        "opcode":0,
        "funct3":0,
        "funct7":0,
        "operands":[]
        },
}

'''Checa se string e um numero inteiro'''
def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

''' Funcao pega uma linha e checa erros de sintaxe, e retorna um dicionario com label, operacao e operandos '''
def split_tokens(line, line_number):
    
    label = ""
    operation = ""
    operands = ""

    # remove comments
    if "#" in line:     
        line = line.split("#")[0]
    
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


def first_pass(code_text):

    contador_pos = 0
    contador_linha = 1

    # To lower case
    code_text = code_text.lower()
    # Separa por linhas
    code_text = code_text.split("\n")


    code_text_aux = list()
    for line in code_text: # para cada linha de codigo
        
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
        
    print(SYMBOL_TABLE)
    return 0;

def check_operands(all_tokens):
    
    operand_match = 0
    operand_type = ""

    if ( len(all_tokens['operands']) == len(INSTRUCTION_TABLE[ all_tokens['operation'] ]['operands']) ):
        for i in range(0,len(INSTRUCTION_TABLE[ all_tokens['operation'] ]['operands'])):
            if (all_tokens['operands'][i] in REGISTER_NAMES):
                operand_type = "register"
            elif (all_tokens['operands'][i] in SYMBOL_TABLE):
                operand_type = "symbol"
            elif ( is_number( all_tokens['operands'][i]) ):
                operand_type = "number"
            else:
                operand_type = "unknown"

            if (INSTRUCTION_TABLE[ all_tokens['operation'] ]['operands'][i] == operand_type):
                operand_match = 1
            else:
                return 0

            print (INSTRUCTION_TABLE[ all_tokens['operation'] ]['operands'][i])
            print( all_tokens['operands'][i] )


    return operand_match


def second_pass(code_text):
    #1
    contador_pos = 0
    contador_linha = 1

    # To lower case
    code_text = code_text.lower()
    # Separa por linhas
    code_text = code_text.split("\n")


    code_text_aux = list()
    for line in code_text: # para cada linha de codigo
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

            print("\n ---"+line+"\n")
            for operand in all_tokens['operands']:
                print(operand)
                if( operand in REGISTER_NAMES):
                    print("Registrador!")
                else:
                    #print("Simbolo")
                    if operand in SYMBOL_TABLE:
                        print("Simbolo existente")
                    else:
                        # if symbol is number or address label:
                        # re.match('(\s{0,})\d{0,}\(\w{1,}\)' ,  operand )  
                        if is_number(operand):
                            print("operando e numero")
                        else:
                            # s[s.find("(")+1:s.find(")")]
                            print("Erro. Simbolo inexistente. linha "+ str(contador_linha))
                            exit(1)
#print("\n")
    
#    3   -   Procura operacao na tabela de instrucoes
#            Se achou:
#                contador_posicao = contador_posicao + tamanho da instrucao
#                Se numero e tipo dos operandos esta correto entao
#                    gera codigo objeto conforme formato da instrucao
#                Senao: 
#                    Erro, operando invalido

            # procura operacao na taela de instrucoes
            if all_tokens['operation'] in INSTRUCTION_TABLE:
                #print(INSTRUCTION_TABLE[ all_tokens['operation'] ])
                contador_pos = contador_pos + INSTRUCTION_TABLE[ all_tokens['operation'] ]['size']

                #checar numero e tipo dos operandos
                if ( check_operands(all_tokens) ):
                    print("Gerando codigo objeto....")
                    print(INSTRUCTION_TABLE[ all_tokens['operation'] ]['opcode'])
                    '''for i in range(0,len(INSTRUCTION_TABLE[ all_tokens['operation'] ]['operands'])):
                        if (all_tokens['operands'][i] in REGISTER_NAMES):
                            print(REGISTER_NAMES[all_tokens['operands'][i]])
                        elif (all_tokens['operands'][i] in SYMBOL_TABLE):
                            print(REGISTER_NAMES[all_tokens['operands'][i]])
                        elif ( is_number( all_tokens['operands'][i]) ):
                            print(  all_tokens['operands'][i] )
                        else:
                            print("op unknown")'''                    

                    # gera codigo objeto
                    '''                       
                        funct7 rs2 rs1 funct3 rd opcode R-type
                        imm[11:0] rs1 funct3 rd opcode I-type
                        imm[11:5] rs2 rs1 funct3 imm[4:0] opcode S-type
                        imm[31:12] rd opcode U-type
                    '''

                    # checa tipo
                    if (INSTRUCTION_TABLE[ all_tokens['operation'] ]['type'] == "r" ):
                        print("___instrucao tipo r______")
                        instr = INSTRUCTION_TABLE[ all_tokens['operation'] ]['funct7'] + REGISTER_NAMES[ all_tokens['operands'][1] ]+REGISTER_NAMES[ all_tokens['operands'][2] ] + INSTRUCTION_TABLE[ all_tokens['operation'] ]['funct3'] + REGISTER_NAMES[ all_tokens['operands'][0] ] + INSTRUCTION_TABLE[ all_tokens['operation'] ]['opcode']                        
                        print( instr + "  tam:"+ str(len(instr))  )
                    elif (INSTRUCTION_TABLE[ all_tokens['operation'] ]['type'] == "i" ):
                        print("____instrucao tipo i____")
                        # checar se imediato eh positivo ou negativo e se ultrapassa o 12 bits
                        if( int(all_tokens['operands'][2][0])>0  ):
                            val_sign = "0"
                        else:
                            val_sign = "1"
                        immediate = ("{:"+val_sign+">12b}").format(int(all_tokens['operands'][2]))
                        instr = immediate + REGISTER_NAMES[ all_tokens['operands'][1] ]+ INSTRUCTION_TABLE[ all_tokens['operation'] ]['funct3'] + REGISTER_NAMES[ all_tokens['operands'][0] ]+ INSTRUCTION_TABLE[ all_tokens['operation'] ]['opcode']
                        if(  len(immediate) > 12 ):
                            print("Erro: Immediate value ")
                        print( instr[0:32] + "  tam:"+ str(len(instr[0:32]))  )

                    elif (INSTRUCTION_TABLE[ all_tokens['operation'] ]['type'] == "s" ):
                        print("instrucao tipo s")
                    elif (INSTRUCTION_TABLE[ all_tokens['operation'] ]['type'] == "u" ):
                        print("instrucao tipo u")
                    elif (INSTRUCTION_TABLE[ all_tokens['operation'] ]['type'] == "sb" ):
                        print("instrucao tipo sb")
                    elif (INSTRUCTION_TABLE[ all_tokens['operation'] ]['type'] == "uj" ):
                        print("instrucao tipo uj")
                    else:
                        print("instrucao tipo errado")

                else:
                    # erro, operando invalido
                    print("Erro: Operando inválido. linha "+str(contador_linha))
                    exit()
#    4   -   Senao:
#                Procura operacao na tabela de diretivas
#                Se achou:
#                    Chama subrotina que executa a diretiva
#                    Contador_posicao = valor retornado pela subrotina
#                Senao: 
#                    Erro, operacao nao identificada
#            Contador_linha = contador_linha + 1




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
label1:ADDI t1, t0, 7657557676
ADDI  t1 , t0, 2
ADDI  t1 , t0, 442

label2:ADDI t1, t0,  443'''


#print(code)
#print("\n")

print("Primeira Passsagem\n")
fp_ret = first_pass(code3)
print("\n")

if fp_ret == 0 :

    #print(SYMBOL_TABLE)
    print("------  Segunda Passsagem\n")
    sp_ret = second_pass(code3)

    #print( "!!!!! ----- print teste " )
    #print(  INSTRUCTION_TABLE['addi']['operands']  )

#print(scanner(processed_code))
