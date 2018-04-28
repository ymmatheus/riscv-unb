'''

    TODO:

        - Implementar diretivas
        - Implementar imediato em hex e bin        
        - Implementar montagem das instruções com syntaxe label(registrador), num(registrador)
        - Implementar pseudo instrucoes
        - Verificar se ta certo a montagem das instrucoes tipo S e SB
        - Melhorar mensagens de erro/warnings
            - Estabelecer códigos para os erros


'''

from utils import settings, instructions, utilities
from utils.utilities import bcolors as clrs

import re

SYMBOL_TABLE = {}
VALUE_TABLE = {}

DIRECTIVES_TABLE = [ ".section" , ".data" , ".text" , ".rodata" , ".bss" , ".equ", ".string" , ".asciz" , ".zero" , ".byte" ]

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
            tokens_op = tokens[1]
        else:
            tokens_op = line

        tokens = tokens_op.split(" ", 1)
        if len(tokens) > 1:
            operation, operands_raw = tokens
        else:
             WARNINGS_ERRORS.insert(len(WARNINGS_ERRORS), "Error: Invalid code. Line: " + str(line_number))
             return -1
        operands = operands_raw.split(",")

        # check if label is one word 
        if len(label.split(" ")) > 1 :
            # print("Syntax Error: More than one word for label before symbol ':'. Line: " + str(line_number))
            WARNINGS_ERRORS.insert(len(WARNINGS_ERRORS),"Syntax Error: More than one word for label before symbol ':'. Line: " + str(line_number))

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
        
        # remove os espacos do inicio e final
        line = line.strip()

        # ignora se for comentario ou linha vazia   
        if(  line == ""  or  line[0]=="#"):
            pass
        else:


            # se tiver diretiva
            if "." in line:

                # count number of directives in line
                n_directives = 0
                for c in line:
                    if "." == c:
                        n_directives=n_directives+1

                # if there is more than 1 directive in the line, break into multiple, if not do nothing
                ################################################
                # TODO
                ################################################

                # sanitize line
                #     remove comments
                sanitized_directive = line.split("#")[0]

                # separate directives and arguments
                directives_separated = sanitized_directive.split(" ")

                # join list items if they are part of a string
                ### check if there are strings
                quote_indexes = [c[0] for c in enumerate(directives_separated) if "\"" in c[1]]
                if len(quote_indexes):

                    if len(quote_indexes) == 1:
                        n_of_quotes = directives_separated[quote_indexes[0]].count("\"")
                    if len(quote_indexes) == 2:
                        n_of_quotes = 0
                        print("qwqweqwe"+str(quote_indexes))
                        for i in range(quote_indexes[0], quote_indexes[1]+1):
                            n_of_quotes = n_of_quotes + directives_separated[i].count("\"")
                   

                    # if there are quote marks in more than 2 elements of list its an error
                    if len(quote_indexes) > 2:
                        WARNINGS_ERRORS.insert(len(WARNINGS_ERRORS),"Error: Syntax unexpected number of \". Line "+str(contador_linha))
                        return -1
                    ### count number of strings, error if more than one
                    if n_of_quotes > 2 :
                        WARNINGS_ERRORS.insert(len(WARNINGS_ERRORS),"Error: More than one string. Line "+str(contador_linha))
                        return -1
                    if n_of_quotes == 1:
                        WARNINGS_ERRORS.insert(len(WARNINGS_ERRORS),"Error: Syntax unexpected number of \". Line "+str(contador_linha))
                        return -1
                    
                    if len(quote_indexes) == 2:
                        aux_list =[]
                        # copy strings to an aux list
                        for i in range(quote_indexes[0], quote_indexes[1]+1):
                            aux_list.append(directives_separated[i])
                        # delete from original list
                        #print("aux list:  "+str(aux_list))
                        for i in range(quote_indexes[0], quote_indexes[1]+1):
                            directives_separated.pop(quote_indexes[0])
                        # join aux list to the original list with whole string in one item
                        directives_separated.insert(quote_indexes[0], ' '.join(aux_list))



                # check directive table
                #    check which directive part is the command itself
                for directive_candidate in directives_separated:
                    #print(directive_candidate)
                    if "." in directive_candidate:
                        directive = directive_candidate

                #print("----"+directive+"\n\n")
        		# directive process

                pass

            
            # se nao for diretiva
            else:
	            all_tokens = split_tokens(line, contador_linha)
	            

	            # Se split_tokens retornar erro, retorna erro para a main
	            if all_tokens == -1:
	                return -1
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
	                        WARNINGS_ERRORS.insert(len(WARNINGS_ERRORS),"Error: Duplicated Symbol. Line "+str(contador_linha))
	                        
	                        return -1
	                    else:
	                        # insere rotulo e contador_posicao na tablea de simbolos
	                        SYMBOL_TABLE[ all_tokens['label'] ] = contador_pos;

	                # procura operacao na tabela de instrucoes
	                if all_tokens['operation'] in instructions.INSTRUCTION_TABLE_REVERSE:
	                    #print("incrementa pos "+ str(instructions.INSTRUCTION_TABLE_REVERSE[all_tokens['operation']]['size']))
	                    contador_pos = contador_pos + instructions.INSTRUCTION_TABLE_REVERSE[all_tokens['operation']]['size']
	                else:
	                    if all_tokens['operation'] in DIRECTIVES_TABLE:
	                        pass
	                        #DIRECTIVES_TABLE[all_tokens['operation']]
	                        #contador_pos = x
	                    else:
	                        WARNINGS_ERRORS.insert(len(WARNINGS_ERRORS),"Error: Operation "+ str(all_tokens['operation']) + " not recognized. Line:"+str(contador_linha))
	                        # print("Error: Operation "+ str(all_tokens['operation']) + " not recognized. Line:"+str(contador_linha)  )
	                        return -1
	            contador_linha = contador_linha + 1

    return 0;

def check_operands(all_tokens, SYMBOL_TABLE):
    
    instruction_type = instructions.INSTRUCTION_TABLE_REVERSE[ all_tokens['operation'] ]['type'] 

    # tipo R: 3 argumentos, 3 registradores
    print(all_tokens)
    print(len(all_tokens['operands']))
    if ( instruction_type == "r" and len(all_tokens['operands']) == 3 ):
        for i in range(0,len(all_tokens['operands'])): 
            if ( all_tokens['operands'][i] not in settings.REGISTER_NAMES ):
                return -1

    # tipo I, S, B: 3 argumentos, 2 registradores e 1 imediato    
    elif ( (instruction_type == "i" or instruction_type == "s" or instruction_type == "b" ) and len(all_tokens['operands']) == 3 ):
        if (all_tokens['operands'][0] not in settings.REGISTER_NAMES or all_tokens['operands'][1] not in settings.REGISTER_NAMES ):
            return -1
        if (  utilities.is_number(all_tokens['operands'][2]) == False and all_tokens['operands'][2] not in SYMBOL_TABLE ):
            return -1

    # tipo U, J: 2 argumentos, 1 registrador e 1 imediato
    elif ( (instruction_type == "u" or instruction_type == "j" ) and len(all_tokens['operands']) == 2 ):

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
#    2   -   Para cada operando que e simbolo
#            Procura operando na TS
#            Se nao achou: 
#                Erro, simbolo indefinido

            # print("\n\n\n\t-"+str(contador_linha)+"--"+line+"\n")
            for operand in all_tokens['operands']:
                #print(operand)
                # se for registrador
                if( operand in settings.REGISTER_NAMES):
                    pass
                    #print("Registrador!")
                #se for simbolo e registrador
                elif re.match("[a-zA-Z0-9]+\(([^)]+)\)", operand, re.M|re.I) :
                    

                    # capture register
                    register_capture = re.search( "\((.*)\)"  , operand, re.M|re.I)
                    register_capture = register_capture.group(1)
                    

                    # immediate register
                    immediate_capture = re.search( "(.*?)\(\w+"  , operand, re.M|re.I)
                    immediate_capture = immediate_capture.group(1)
                    
                    # se a captura de registrador for registrador e a captura de imediato for um numero ou um simbolo da tabela ok senao erro
                    if register_capture in settings.REGISTER_NAMES and  (immediate_capture in SYMBOL_TABLE or utilities.is_number(immediate_capture)) :
                        pass

                    else:
                        WARNINGS_ERRORS.insert(len(WARNINGS_ERRORS), "Erro. Operando inválido. linha "+ str(contador_linha) )
                        return 1


                # se for simbolo
                else:
                    #print("Simbolo")
                    if operand in SYMBOL_TABLE:
                        pass
                        #print("Simbolo existente")
                    else:
                        # if symbol is number or address label:
                        # re.match('(\s{0,})\d{0,}\(\w{1,}\)' ,  operand )  
                        if utilities.is_number(operand):
                            pass
                            #print("operando e numero")
                        else:
                            # s[s.find("(")+1:s.find(")")]
                            # print("Erro. Simbolo inexistente. linha "+ str(contador_linha))
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
                                        
                        instr = funct7 + operand1 + operand2 + funct3 + operand0 + opcode

                    elif ( instruction_type == "i" ):
                        #    imm[11:0] rs1 funct3 rd opcode I-type
                        # print("____instrucao tipo i____")
                        # print(all_tokens['operands'])
                        if( utilities.is_number(all_tokens['operands'][2]) ):
                            immediate = utilities.s2bin(  int(all_tokens['operands'][2])  , 12)
                        elif( all_tokens['operands'][2] in SYMBOL_TABLE ):
                            #print("es label")
                            #print(SYMBOL_TABLE[all_tokens['operands'][2]])
                            immediate = utilities.s2bin(  int(SYMBOL_TABLE[all_tokens['operands'][2]])  , 12)

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
                            
                            # capture register
                            register_capture = re.search( "\((.*)\)"  , all_tokens['operands'][1], re.M|re.I)
                            operand2 = settings.REGISTER_NAMES[ register_capture.group(1) ]
                            
                            # immediate register
                            immediate_capture = re.search( "(.*?)\(\w+"  , all_tokens['operands'][1], re.M|re.I)
                            immediate = utilities.s2bin(  int( immediate_capture.group(1) )  , 12)                         

                        else:
                            immediate = utilities.s2bin(  int(all_tokens['operands'][2])  , 12)                        
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
                                instr = immediate[0]+immediate[2:7] + operand2 + operand1 + funct3 + immediate[7:12] + immediate[1]+ opcode
                                
                    elif ( instruction_type == "u" or instruction_type == "uj" ):
                        #    imm[31:12] rd opcode U-type
                        immediate = utilities.s2bin(  int(all_tokens['operands'][1])  , 20)
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


#print(code)
#print("\n")
def assemble(code):
    
    global WARNINGS_ERRORS

    # Entrada: Recebe o programa completo
    # Saida: Dicionario com dados de codigo, memoria e mensagens de erros

    # Algoritmo de duas passagens
    
    fp_ret = first_pass(code)
    if fp_ret == 0:
        sp_ret = second_pass(code)

    errors_ret = WARNINGS_ERRORS 
    WARNINGS_ERRORS = list()
    


    return {"code":settings.code_memory, "memory":settings.data_memory, "errors":errors_ret}
