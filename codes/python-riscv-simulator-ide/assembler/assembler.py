'''

    TODO:

        - Implementar diretivas
        - Implementar imediato em hex e bin        
        - Implementar montagem das instruções com syntaxe label(registrador), num(registrador)
        - Implementar pseudo instrucoes

'''

from utils import settings, instructions, utilities
from utils.utilities import bcolors as clrs

import re

SYMBOL_TABLE = {}
VALUE_TABLE = {}

DIRECTIVES_TABLE = [ ".section" , ".data" , ".text" , ".rodata" , ".bss" , ".equ", ".string" , ".asciiz" , ".zero" , ".byte" , ".word"]

# Lista de erros e warning do montador
WARNINGS_ERRORS = list()

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
                # print("Syntax Error: More than one label in the same line. Line: " + str(line_number))
                WARNINGS_ERRORS.insert(len(WARNINGS_ERRORS), "Syntax Error: More than one label in the same line. Line: " + str(line_number))
                return -1            

            label = tokens[0]
            tokens_op = tokens[1].strip()

            # check if label is one word 
            if len(label.split(" ")) > 1 :
                # print("Syntax Error: More than one word for label before symbol ':'. Line: " + str(line_number))
                WARNINGS_ERRORS.insert(len(WARNINGS_ERRORS),"Syntax Error: More than one word for label before symbol ':'. Line: " + str(line_number))

                return -1
        # if there isnt a label
        else:
            tokens_op = line



        if label and not tokens_op:
            # if there is only a label in the current line, skip everything and concatenate with next line
            operands = []
            operation = []
            return 2 # code for concatenation
        else:
            tokens = tokens_op.split(" ", 1)
            
            n_tokens = len(tokens)
            if n_tokens == 1:
                operation = tokens[0]
                operands = []
            elif n_tokens > 1:
                operation, operands_raw = tokens
                operands = operands_raw.split(",")
            else:
                 WARNINGS_ERRORS.insert(len(WARNINGS_ERRORS), "Error: Invalid code. Line: " + str(line_number))
                 return -1
            
            ## Sanitize tokens
            # remove empty spaces on operation
            operation = operation.strip()

            # remove empty spaces of operands
            for i in range( len(operands) ):
                operands[i] = operands[i].strip()

      



    return {"label":label, "operation":operation, "operands":operands }


def first_pass(code_text):

    contador_pos = 0
    contador_pos_mem = 0
    contador_linha = 1

    concat_next_line = 0
    prev_line = ""
    # To lower case
    if "\"" not in code_text:
        code_text = code_text.lower()
    # Separa por linhas
    code_text = code_text.split("\n")


    code_text_aux = list()
    for line in code_text: # para cada linha de codigo
        
        # remove os espacos do inicio e final
        line = line.strip()

        # ignora se for comentario ou linha vazia   
        if(  line == ""  or  line[0]=="#"):
            contador_linha = contador_linha + 1        
        else:

            # concatenate with previous line (label alone)
            if concat_next_line == 1:
                line = prev_line+line
                concat_next_line = 0
                contador_linha = contador_linha + 1
            all_tokens = split_tokens(line, contador_linha)
            #print(all_tokens)
            # Se split_tokens retornar erro, retorna erro para a main
            if all_tokens == -1:
                return -1
            # Set flag to next line to concatenate with this line
            elif all_tokens == 2:                
                prev_line = line
                concat_next_line=1

                
            else:
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
                            # print("Error: Duplicated Symbol. Line "+str(contador_linha))
                            print(all_tokens['label'] )
                            WARNINGS_ERRORS.insert(len(WARNINGS_ERRORS),"Error: Duplicated Symbol. Line "+str(contador_linha))
                            
                            return -1
                        else:
                            # insere rotulo e contador_posicao na tablea de simbolos
                            SYMBOL_TABLE[ all_tokens['label'] ] = ["ADDR",contador_pos+4]; # Adds 4 to get the next instruction

                    # procura operacao na tabela de instrucoes
                    if all_tokens['operation'] in instructions.INSTRUCTION_TABLE_REVERSE:
                        #print("incrementa pos "+ str(instructions.INSTRUCTION_TABLE_REVERSE[all_tokens['operation']]['size']))
                        contador_pos = contador_pos + instructions.INSTRUCTION_TABLE_REVERSE[all_tokens['operation']]['size']
                    else:

                    ######################      DIRECTIVE PROCESSING        ###########################
                        
                        if all_tokens['operation'] in DIRECTIVES_TABLE:
                            
                            directive = all_tokens['operation']

                            if directive == ".data":
                                pass # TODO
                            elif directive == ".text":
                                pass # TODO
                            elif directive == ".word":
                                
                                # check type and number of arguments
                                directive_arguments = all_tokens['operands'][0]
                                if utilities.is_number( directive_arguments  ) :                                    
                                    SYMBOL_TABLE[ all_tokens['label'] ] = ["DATA", utilities.u2bin(contador_pos_mem,32) ]
                                    VALUE_TABLE[utilities.u2bin(contador_pos_mem,32)] = int(directive_arguments)
                                    mem_data = utilities.s2bin(int(directive_arguments),32)                                    
                                    settings.data_memory[contador_pos_mem] = mem_data[-8:]
                                    settings.data_memory[contador_pos_mem+1] = mem_data[-16:-8]
                                    settings.data_memory[contador_pos_mem+2] = mem_data[-24:-16]
                                    settings.data_memory[contador_pos_mem+3] = mem_data[-32:-24]
                                    contador_pos_mem=contador_pos_mem+4
                                else:
                                    WARNINGS_ERRORS.insert(len(WARNINGS_ERRORS),"Syntax Error: Wrong number or type of argument. Line "+str(contador_linha))
                            #print(all_tokens)
                            #DIRECTIVES_TABLE[all_tokens['operation']]
                            #contador_pos = x

                            elif directive == ".string" or directive == ".asciiz" or directive == ".ascii" :
                                
                                s = re.findall('"([^"]*)"', line)
                                #print(list(s))
                                if len(s) == 1:
                                    s = s[0]
                                    # generate list of ascii codes
                                    ascii_list = []
                                    for ascii_code in bytearray(s, 'ascii'):                                        
                                        ascii_list.append(utilities.u2bin(  ascii_code   , 8  ))

                                    # process list escaping e.g. \n, \t
                                        # '00101111' = '/'
                                        # https://en.wikipedia.org/wiki/Escape_sequences_in_C

                                    escape_dict = {'01100001':'00000111', '01100010':'00001000', '01100110':'00001100', '01101110':'00001010', '01110010': '00001101', '01110100' : '00001001', '01110110':'00001011', '01011100':'01011100', '00100111':'0100111', '00100010':'00100010'}
                                    #print(ascii_list)

                                    ascii_list_len = len(ascii_list)                                    
                                    escaped_ascii_list = []
                                    escape_flag = False
                                    ascii_list_index = 0
                                    for ch in ascii_list:
                                        
                                        if ch == '01011100': # If the character is a backslash                                            
                                            if (ascii_list_index+1 < ascii_list_len) and ascii_list[ascii_list_index+1] in escape_dict:                                                
                                                escaped_ascii_list.append(escape_dict[ch])
                                                escape_flag = True
                                            else:
                                                escaped_ascii_list.append('01011100')
                                        else:
                                            if escape_flag == False:
                                                escaped_ascii_list.append(ch)
                                            else:
                                                escape_flag = False
                                        ascii_list_index = ascii_list_index + 1
                                    #print(escaped_ascii_list)
                                    #print(len(escaped_ascii_list))
                                    data_mem_index = 0
                                    for ch in range(len(escaped_ascii_list)) :
                                        if (contador_pos_mem+data_mem_index < settings.DATA_MEMORY_SIZE):
                                            settings.data_memory[contador_pos_mem+data_mem_index] = escaped_ascii_list[ch]

                                            data_mem_index = data_mem_index + 1
                                        else:
                                            WARNINGS_ERRORS.insert(len(WARNINGS_ERRORS),"Error: Insufficient memory. Line:"+str(contador_linha))
                                            return -1
                                    #settings.data_memory[contador_pos_mem+data_mem_index] = "00000000"

                                    current_mem_pos = contador_pos_mem+data_mem_index+1
                                    #contador_pos_mem = current_mem_pos
                                    contador_pos_mem = (int(current_mem_pos/4) + current_mem_pos%4)*4 # update the memory index to next aligned word ?(should it be like this?)
                                    #print(current_mem_pos)
                                    #print(contador_pos_mem)

                                else:
                                    WARNINGS_ERRORS.insert(len(WARNINGS_ERRORS),"Error: Incorrect number of string. Line:"+str(contador_linha))
                                    return -1    
                                

                            else:
                                WARNINGS_ERRORS.insert(len(WARNINGS_ERRORS),"Error: Operation "+ str(all_tokens['operation']) + " not recognized. Line:"+str(contador_linha))
                                # print("Error: Operation "+ str(all_tokens['operation']) + " not recognized. Line:"+str(contador_linha)  )
                                return -1    



                        else:
                            WARNINGS_ERRORS.insert(len(WARNINGS_ERRORS),"Error: Operation "+ str(all_tokens['operation']) + " not recognized. Line:"+str(contador_linha))
                            # print("Error: Operation "+ str(all_tokens['operation']) + " not recognized. Line:"+str(contador_linha)  )
                            return -1
            contador_linha = contador_linha + 1
    return 0;

def check_operands(all_tokens, SYMBOL_TABLE):
    
    
    # Special cases formats
    if all_tokens['operation'] == 'ecall' or all_tokens['operation'] == 'ebreak' :
        return 0

    if all_tokens['operation'] == 'lw' or all_tokens['operation'] == 'sw' and len(all_tokens['operands']) == 2:
        immediate_register_get = re.match("([a-zA-Z0-9\_]+)\(([^)]+)\)", all_tokens['operands'][1], re.M|re.I)
        print(immediate_register_get.group(1))
        print(immediate_register_get.group(2))
        rd = all_tokens['operands'][0]
        all_tokens['operands'] = [rd, immediate_register_get.group(2),immediate_register_get.group(1)]
    instruction_type = instructions.INSTRUCTION_TABLE_REVERSE[ all_tokens['operation'] ]['type'] 

    print(all_tokens['operands'])
    # tipo R: 3 argumentos, 3 registradores
    #print(all_tokens)
    #print(len(all_tokens['operands']))
    

    if ( instruction_type == "r" and len(all_tokens['operands']) == 3 ):
        for i in range(0,len(all_tokens['operands'])): 
            if ( all_tokens['operands'][i] not in settings.REGISTER_NAMES ):
                return -1

    # tipo I, S, B: 3 argumentos, 2 registradores e 1 imediato    
    elif ( (instruction_type == "i" or instruction_type == "s" or instruction_type == "sb" ) and len(all_tokens['operands']) == 3 ):

        if (all_tokens['operands'][0] not in settings.REGISTER_NAMES or all_tokens['operands'][1] not in settings.REGISTER_NAMES ):
            return -1
        if (  utilities.is_number(all_tokens['operands'][2]) == False and all_tokens['operands'][2] not in SYMBOL_TABLE ):
            return -1

    # tipo U, J: 2 argumentos, 1 registrador e 1 imediato
    elif ( (instruction_type == "u" or instruction_type == "uj" ) and len(all_tokens['operands']) == 2 ):

        if (all_tokens['operands'][0] not in settings.REGISTER_NAMES ):
            return -1
        if (  utilities.is_number(all_tokens['operands'][1]) == False and all_tokens['operands'][1] not in SYMBOL_TABLE ):
            return -1

    elif (instruction_type == "s") and len(all_tokens['operands']) == 2 :
        
        if (all_tokens['operands'][0] not in settings.REGISTER_NAMES ):
            return -1

        # capture register
        register_capture = re.search( "\((.*)\)"  , all_tokens['operands'][1], re.M|re.I)
        register_capture = register_capture.group(1)
        
        # immediate register
        immediate_capture = re.search( "(.*?)\(\w+"  , all_tokens['operands'][1], re.M|re.I)
        immediate_capture = immediate_capture.group(1)

        if( utilities.is_number( immediate_capture ) == False and immediate_capture not in SYMBOL_TABLE ):
            return -1

        if register_capture not in settings.REGISTER_NAMES:
            return -1

    else: 
        return -1

    return 0


def second_pass(code_text):
    #   1   -   Inicializa variaveis
    #
    #

    contador_pos = 0
    contador_linha = 1

    # To lower case
    if '"' not in code_text:
        code_text = code_text.lower()
    # Separa por linhas
    code_text = code_text.split("\n")
    code_memory_counter = 0
    code_text_aux = list()
    for line in code_text: # para cada linha de codigo
        # remoe os espacos do inicio e final
        line = line.strip()

        # ignora se for comentario ou linha vazia ou conter diretiva
        if(line == "" or line[0]=="#" or "." in line):
            contador_linha=contador_linha+1
        else:

            all_tokens = split_tokens(line, contador_linha)
            
            if all_tokens == 2:
                contador_linha = contador_linha + 1
            else:
                
#    2   -   Para cada operando que e simbolo
#            Procura operando na TS
#            Se nao achou: 
#                Erro, simbolo indefinido

                # print("\n\n\n\t-"+str(contador_linha)+"--"+line+"\n")
                
                for operand in all_tokens['operands']:
                
                    immediate_register_get = re.match("([a-zA-Z0-9\_]+)\(([^)]+)\)", operand, re.M|re.I)
                    if( operand in settings.REGISTER_NAMES):
                        pass
                        #print("Registrador!")
                    #se for simbolo e registrador
                    elif immediate_register_get:
                        

                        # immediate register
                        immediate_capture = immediate_register_get.group(1)
                        print(immediate_capture)

                        # capture register                
                        register_capture = immediate_register_get.group(2)
                        print(register_capture)


                     
                        # se a captura de registrador for registrador e a captura de imediato for um numero ou um simbolo da tabela ok senao erro
                        if register_capture in settings.REGISTER_NAMES and  (immediate_capture in SYMBOL_TABLE or utilities.is_number(immediate_capture)) :
                            pass

                        else:
                            WARNINGS_ERRORS.insert(len(WARNINGS_ERRORS), "Erro. Operando inválido. linha "+ str(contador_linha) )
                            return 1


                    # se for simbolo
                    else:
                        #print("Simbolo")
                        if operand in SYMBOL_TABLE or all_tokens['operation'] == 'ecall':
                            
                            pass
                            #print("Simbolo existente")                    
                        else:
                            # if symbol is number or address label:
                            # re.match('(\s{0,})\d{0,}\(\w{1,}\)' ,  operand )  
                            if utilities.is_number(operand):
                                pass
                                #print("operando e numero")
                            else:
                                WARNINGS_ERRORS.insert(len(WARNINGS_ERRORS), "Erro. Simbolo inexistente. linha "+ str(contador_linha) )
                                return 1
    #print("\n")
        
    #    3   -   Procura operacao na tabela de instrucoes
    #            Se achou:
    #                contador_posicao = contador_posicao + tamanho da instrucao
    #                Se numero e tipo dos operandos esta correto entao
    #                    gera codigo objeto conforme formato da instrucao
    #                Senao: 
    #                    Erro, operando invalido

                # procura operacao na taela de instrucoes

                if all_tokens['operation'] in instructions.INSTRUCTION_TABLE_REVERSE:
                    #print(instructions.INSTRUCTION_TABLE_REVERSE[ all_tokens['operation'] ])
                    contador_pos = contador_pos + instructions.INSTRUCTION_TABLE_REVERSE[ all_tokens['operation'] ]['size']

                    #checar numero e tipo dos operandos
                    if ( check_operands(all_tokens, SYMBOL_TABLE) == 0):
                        #print("Gerando codigo objeto....")
                        # gera codigo objeto
                        # checa tipo
                        print("segunda vez")
                        print(all_tokens['operands'])
                        instruction_type = instructions.INSTRUCTION_TABLE_REVERSE[ all_tokens['operation'] ]['type']
                        
                        opcode = instructions.INSTRUCTION_TABLE_REVERSE[ all_tokens['operation'] ]['opcode']
                        #print( all_tokens['operands'] )
                        if ( instruction_type == "r" ):
                            #    funct7 rs2 rs1 funct3 rd opcode R-type
                            # print("___instrucao tipo r______")

                            funct3 = instructions.INSTRUCTION_TABLE_REVERSE[ all_tokens['operation'] ]['funct3']
                            funct7 = instructions.INSTRUCTION_TABLE_REVERSE[ all_tokens['operation'] ]['funct7']
                            operand0 = settings.REGISTER_NAMES[ all_tokens['operands'][0] ]
                            operand1 = settings.REGISTER_NAMES[ all_tokens['operands'][1] ]
                            operand2 = settings.REGISTER_NAMES[ all_tokens['operands'][2] ]                        
                                            
                            instr = funct7  + operand2 + operand1 + funct3 + operand0 + opcode

                        elif ( instruction_type == "i" ):
                            #    imm[11:0] rs1 funct3 rd opcode I-type
                            # print("____instrucao tipo i____")
                            # print(all_tokens['operands'])
                            if all_tokens['operation'] == 'ecall':
                                immediate = '000000000000'
                                operand1 = '00000'
                                operand0 = '00000'
                                funct3 = instructions.INSTRUCTION_TABLE_REVERSE[ all_tokens['operation'] ]['funct3']
                            else:    
                                if( utilities.is_number(all_tokens['operands'][2]) ):
                                    immediate = utilities.s2bin(  int(all_tokens['operands'][2])  , 12)
                                elif( all_tokens['operands'][2] in SYMBOL_TABLE ):                                                            
                                    if SYMBOL_TABLE[all_tokens['operands'][2]][0]=="DATA":                                    
                                        immediate = SYMBOL_TABLE[all_tokens['operands'][2]][1][-12:]

                                funct3 = instructions.INSTRUCTION_TABLE_REVERSE[ all_tokens['operation'] ]['funct3']
                                operand0 = settings.REGISTER_NAMES[ all_tokens['operands'][0] ]                
                                operand1 = settings.REGISTER_NAMES[ all_tokens['operands'][1] ]

                                # checar se imediato ultrapassa o 12 bits                        
                                if( len(immediate) > 12  ):
                                    # print("Error: Imediato não pode ser representado .linha "+str(contador_linha))
                                    WARNINGS_ERRORS.insert(len(WARNINGS_ERRORS), "Error: Imediato não pode ser representado .linha "+str(contador_linha) )
                                    return -1
                                else: # Se esta ok checa se nao eh shift e dps monta a instrucao
                                    if( all_tokens['operation']  == "srli" ):
                                        immediate[0:7] = "0000000"
                                        immediate[7:13] = utilities.s2bin(  int(all_tokens['operands'][2])  , 5)
                                    elif( all_tokens['operation'] == "srai" ):
                                        immediate[0:7] = "0100000"
                                        immediate[7:13] = utilities.s2bin(  int(all_tokens['operands'][2])  , 5)

                            instr = immediate + operand1 + funct3 + operand0 + opcode

                        elif ( instruction_type == "s" or instruction_type == "sb" ):
                            
                            #    imm[11:5] rs2 rs1 funct3 imm[4:0] opcode S-type

                            funct3 = instructions.INSTRUCTION_TABLE_REVERSE[ all_tokens['operation'] ]['funct3']
                            operand1 = settings.REGISTER_NAMES[ all_tokens['operands'][0] ]
                           
                            if ( instruction_type == "s"):

                                if len(all_tokens['operands']) == 3:
                                    print(all_tokens['operands'])
                                    operand2 = settings.REGISTER_NAMES[ all_tokens['operands'][1] ]

                                    if( utilities.is_number(all_tokens['operands'][2]) ):
                                        immediate = utilities.s2bin(  int(all_tokens['operands'][2])  , 12)
                                    elif( all_tokens['operands'][2] in SYMBOL_TABLE ):                                                            
                                        if SYMBOL_TABLE[all_tokens['operands'][2]][0]=="DATA":                                    
                                            immediate = SYMBOL_TABLE[all_tokens['operands'][2]][1][-12:]

                                    print(immediate)
                                elif len(all_tokens['operands']) == 2:

                                    # TODO: implement regular expression for flag(xR) syntax 
                                
                                    print(all_tokens['operands'][1])
                                    register_capture = re.search( "\((.*)\)"  , all_tokens['operands'][1], re.M|re.I)
                                    immediate_capture = re.search( "(.*?)\(\w+"  , all_tokens['operands'][1], re.M|re.I)
                                    if register_capture and immediate_capture:
                                        operand2 = settings.REGISTER_NAMES[ register_capture.group(1) ]
                                        immediate = utilities.s2bin(  int( immediate_capture.group(1) )  , 12)                         
                                        print(immediate)
                                        print(operand2)
                                    else:
                                        print(all_tokens['operands'][1])
                                        
                                    
                            else:


                                if all_tokens['operands'][2] in SYMBOL_TABLE:
                                    #print( SYMBOL_TABLE[all_tokens['operands'][2]][1] )
                                    label_addr = SYMBOL_TABLE[all_tokens['operands'][2]][1] - contador_pos
                                immediate = utilities.s2bin(  int(label_addr/2)  , 12) # Divided by 4 = shift arith right by 2                       
                                operand2 = settings.REGISTER_NAMES[ all_tokens['operands'][1] ]
                            
                            # checar se imediato ultrapassa o 12 bits                        
                            if( len(immediate) > 12  ):
                                WARNINGS_ERRORS.insert(len(WARNINGS_ERRORS),"Error: Imediato não pode ser representado .linha "+str(contador_linha))
                                # print("Error: Imediato não pode ser representado .linha "+str(contador_linha))
                                exit(1)
                            else:
                                # TODO: verificar se ta certo
                                instr = immediate[0:7] + operand2 + operand1 + str(funct3) + immediate[7:13] + opcode

                                if( instruction_type == "sb" ): # embaralha alguns bits
                                    instr = immediate[0]+immediate[2:8] + operand2 + operand1 + funct3 + immediate[8:13] + immediate[1]+ opcode

                        elif ( instruction_type == "u" or instruction_type == "uj" ):
                            #    imm[31:12] rd opcode U-type

                            #print(all_tokens['operands'])
                            if all_tokens['operands'][1] in SYMBOL_TABLE:
                            #    print(all_tokens['operands'])
                                #print( SYMBOL_TABLE[all_tokens['operands'][1]] )
                                label_addr = SYMBOL_TABLE[all_tokens['operands'][1]][1] - contador_pos

                            immediate = utilities.s2bin(  int(label_addr/2)  , 20) # Divided by 2 = shift arith right by 2                       
                            #immediate = utilities.s2bin(  int(all_tokens['operands'][1])/4  , 20) # Divided by 4 = shift arith right by 2
                            operand0 = settings.REGISTER_NAMES[ all_tokens['operands'][0] ]
                            # checar se imediato ultrapassa o 12 bits                        
                            if( len(immediate) > 20 ):
                                WARNINGS_ERRORS.insert(len(WARNINGS_ERRORS), "Error: Imediato não pode ser representado .linha "+str(contador_linha) )
                                #print("Error: Imediato não pode ser representado .linha "+str(contador_linha))
                                return -1
                            else:
                                instr = immediate + operand0 + opcode
                                if( instruction_type == "uj" ): # embaralha alguns bits
                                    im = immediate # apenas apra facilitar leitura
                                    instr = im[0] + im[10:20] + im[9] + im[1:9] + operand0 + opcode

                                    # 0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19
                                    # 20 19 18 17 16 15 14 13 12 11 10  9  8  7  6  5  4  3  2  1

                        else:
                            WARNINGS_ERRORS.insert(len(WARNINGS_ERRORS), "Erro: Tipo da instrucao invalido. linha "+str(contador_linha) )
                            print("Erro: Tipo da instrucao invalido. linha "+str(contador_linha))

                        # print( instr[0:32] + "  tam:"+ str(len(instr[0:32]))  )
                        settings.code_memory[code_memory_counter] = instr 
                        code_memory_counter = code_memory_counter + 1
                    else:
                        # erro, operando invalido
                        #print(all_tokens)
                        WARNINGS_ERRORS.insert(len(WARNINGS_ERRORS), "Erro: Operando inválido. linha "+str(contador_linha) )
                        WARNINGS_ERRORS.insert(len(WARNINGS_ERRORS), str(all_tokens) )
                        print("Erro: Operando inválido. linha "+str(contador_linha))
                        return -1
    #    4   -   Senao:
    #                Procura operacao na tabela de diretivas
    #                Se achou:
    #                    Chama subrotina que executa a diretiva
    #                    Contador_posicao = valor retornado pela subrotina
    #                Senao: 
    #                    Erro, operacao nao identificada
    #            Contador_linha = contador_linha + 1

                else: # se nao tiver instrucao, procura em diretivas
                    if all_tokens['operation'] in DIRECTIVES_TABLE: 
                        pass
                        #DIRECTIVES_TABLE[all_tokens['operation']]
                        #contador_pos = x
                    else: # senao existe instrucao nem diretiva lanca erro
                        WARNINGS_ERRORS.insert(len(WARNINGS_ERRORS), "Error: Operation "+ str(all_tokens['operation']) + " not recognized. Line:"+str(contador_linha) )
                        # print("Error: Operation "+ str(all_tokens['operation']) + " not recognized. Line:"+str(contador_linha)  )
                        return -1
                contador_linha = contador_linha + 1

    return 0

def instruction_from_binary(assembled_line):

    settings.opcode = assembled_line[25:32]
    settings.rd = assembled_line[20:25]
    settings.funct3 = assembled_line[17:20]
    settings.rs1 = assembled_line[12:17]
    settings.rs2 = assembled_line[7:12]
    settings.funct7 = assembled_line[0:7]

    settings.imm_i = assembled_line[0]*21 + assembled_line[1:7] + assembled_line[7:11] + assembled_line[11] 
    settings.imm_s = assembled_line[0]*21 + assembled_line[1:7] + assembled_line[20:24] + assembled_line[24]
    settings.imm_b = assembled_line[0]*20 + assembled_line[24] + assembled_line[1:7] + assembled_line[20:24] + "0"
    settings.imm_u = assembled_line[0] + assembled_line[1:12] + assembled_line[12:20] + "0"*12 
    settings.imm_j = assembled_line[0]*12 + assembled_line[12:20] + assembled_line[11] + assembled_line[1:7] + assembled_line[7:11] + "0"

    if settings.opcode in instructions.instruction_table.keys():
        if (instructions.instruction_table[settings.opcode]["type"] == "r"):
        
            instruction_name = instructions.instruction_table[settings.opcode][settings.funct3][settings.funct7]
            return instruction_name + " " + settings.REVERSE_REGISTER_NAMES[settings.rd] + ", " + settings.REVERSE_REGISTER_NAMES[settings.rs2] + ", " + settings.REVERSE_REGISTER_NAMES[settings.rs1]

        elif (instructions.instruction_table[settings.opcode]["type"] == "i"):

            instruction_name = instructions.instruction_table[settings.opcode][settings.funct3]
            return instruction_name + " " + settings.REVERSE_REGISTER_NAMES[settings.rd] + ", " + settings.REVERSE_REGISTER_NAMES[settings.rs1] + ", " + str(utilities.bin2s(settings.imm_i))
        
        elif (instructions.instruction_table[settings.opcode]["type"] == "u"):
        
            instruction_name = instructions.instruction_table[settings.opcode]["inst_name"]
            return instruction_name + " " + settings.REVERSE_REGISTER_NAMES[settings.rd] + ", "+ str(utilities.bin2s(settings.imm_u))
        
        elif (instructions.instruction_table[settings.opcode]["type"] == "uj"):
        
            instruction_name = instructions.instruction_table[settings.opcode]["inst_name"]
            return instruction_name + " " + settings.REVERSE_REGISTER_NAMES[settings.rd] + ", " + str(utilities.bin2s(settings.imm_j))
        elif (instructions.instruction_table[settings.opcode]["type"] == "s"):
        
            instruction_name = instructions.instruction_table[settings.opcode][settings.funct3]
            return instruction_name + " " + settings.REVERSE_REGISTER_NAMES[settings.rs1] + ", " + settings.REVERSE_REGISTER_NAMES[settings.rs2] + ", " + str(utilities.bin2s(settings.imm_s))
        elif (instructions.instruction_table[settings.opcode]["type"] == "sb"):
        
            instruction_name = instructions.instruction_table[settings.opcode][settings.funct3]
            return instruction_name + " " + settings.REVERSE_REGISTER_NAMES[settings.rd] + ", " + settings.REVERSE_REGISTER_NAMES[settings.rs1] + ", " + str(utilities.bin2s(settings.imm_b))
        elif settings.opcode == '0000000':

            instruction_name = "nop"

        else:

            instruction_name = "unknown"


    else:

        instruction_name = "unknown"
    return instruction_name

def assemble(code):
    
    global WARNINGS_ERRORS
    global SYMBOL_TABLE
    global VALUE_TABLE
    # Entrada: Recebe o programa completo
    # Saida: Dicionario com dados de codigo, memoria e mensagens de erros

    # Algoritmo de duas passagens
    
    fp_ret = first_pass(code)
    if fp_ret == 0:
        sp_ret = second_pass(code)

    #print(settings.code_memory)
    #print(SYMBOL_TABLE)

    errors_ret = WARNINGS_ERRORS 
    WARNINGS_ERRORS = list()  


    # Reset global variables for next assemble
    SYMBOL_TABLE = {}
    VALUE_TABLE = {}

    assmebled_info = []
    pc_val = 0
    for assembled_line in settings.code_memory:
        assmebled_info.append({'pc':pc_val, 'hex': "0x"+utilities.bin2hex(assembled_line) , 'instr': instruction_from_binary(assembled_line)})
        pc_val = pc_val + 4

    return {"code":settings.code_memory, "memory":settings.data_memory, "errors":errors_ret, "assembled_info": assmebled_info}
