from utils import settings, instructions, utilities

DIRECTIVES_TABLE = [ ".section" , ".data" , ".text" , ".space" , ".word" , ".ascii" , ".asciiz", ".byte" ]

SYMBOL_TABLE = {}

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
        if(  line == ""  or  line[0]=="#"):
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
                if all_tokens['operation'] in instructions.INSTRUCTION_TABLE_REVERSE:
                    #print("incrementa pos "+ str(instructions.INSTRUCTION_TABLE_REVERSE[all_tokens['operation']]['size']))
                    contador_pos = contador_pos + instructions.INSTRUCTION_TABLE_REVERSE[all_tokens['operation']]['size']
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

    if ( len(all_tokens['operands']) == len(instructions.INSTRUCTION_TABLE_REVERSE[ all_tokens['operation'] ]['operands']) ):
        for i in range(0,len(instructions.INSTRUCTION_TABLE_REVERSE[ all_tokens['operation'] ]['operands'])):
            if (all_tokens['operands'][i] in settings.REGISTER_NAMES):
                operand_type = "register"
            elif (all_tokens['operands'][i] in SYMBOL_TABLE):
                operand_type = "symbol"
            elif ( utilities.is_number( all_tokens['operands'][i]) ):
                operand_type = "number"
            else:
                operand_type = "unknown"

            if (instructions.INSTRUCTION_TABLE_REVERSE[ all_tokens['operation'] ]['operands'][i] == operand_type):
                operand_match = 1
            else:
                return 0

            #print (instructions.INSTRUCTION_TABLE_REVERSE[ all_tokens['operation'] ]['operands'][i])
            #print( all_tokens['operands'][i] )


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
        if(line == "" or line[0]=="#" ):
            pass
        else:

            all_tokens = split_tokens(line, contador_linha)

#    2   -   Para cada operando que e simbolo
#            Procura operando na TS
#            Se nao achou: 
#                Erro, simbolo indefinido

            print("\n\n\n\t---"+line+"\n")
            for operand in all_tokens['operands']:
                #print(operand)
                if( operand in settings.REGISTER_NAMES):
                    pass
                    #print("Registrador!")
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
            if all_tokens['operation'] in instructions.INSTRUCTION_TABLE_REVERSE:
                #print(instructions.INSTRUCTION_TABLE_REVERSE[ all_tokens['operation'] ])
                contador_pos = contador_pos + instructions.INSTRUCTION_TABLE_REVERSE[ all_tokens['operation'] ]['size']

                #checar numero e tipo dos operandos
                if ( check_operands(all_tokens) ):
                    print("Gerando codigo objeto....")
                    print(instructions.INSTRUCTION_TABLE_REVERSE[ all_tokens['operation'] ]['opcode'])

                    # gera codigo objeto
                    # checa tipo
                    if (instructions.INSTRUCTION_TABLE_REVERSE[ all_tokens['operation'] ]['type'] == "r" ):
                        #    funct7 rs2 rs1 funct3 rd opcode R-type
                        print("___instrucao tipo r______")
                        instr = instructions.INSTRUCTION_TABLE_REVERSE[ all_tokens['operation'] ]['funct7'] + settings.REGISTER_NAMES[ all_tokens['operands'][1] ]+settings.REGISTER_NAMES[ all_tokens['operands'][2] ] + instructions.INSTRUCTION_TABLE_REVERSE[ all_tokens['operation'] ]['funct3'] + settings.REGISTER_NAMES[ all_tokens['operands'][0] ] + instructions.INSTRUCTION_TABLE_REVERSE[ all_tokens['operation'] ]['opcode']                        
                        print( instr + "  tam:"+ str(len(instr))  )
                    elif (instructions.INSTRUCTION_TABLE_REVERSE[ all_tokens['operation'] ]['type'] == "i" ):
                        #    imm[11:0] rs1 funct3 rd opcode I-type
                        print("____instrucao tipo i____")
                        # checar se imediato ultrapassa o 12 bits
                        immediate = utilities.s2bin(  int(all_tokens['operands'][2])  , 12)
                        if( len(immediate) >12  ):
                            print("Error: Imediato não pode ser representado .linha "+str(contador_linha))
                            exit(1)
                        else:
                            instr = immediate + settings.REGISTER_NAMES[ all_tokens['operands'][1] ]+ instructions.INSTRUCTION_TABLE_REVERSE[ all_tokens['operation'] ]['funct3'] + settings.REGISTER_NAMES[ all_tokens['operands'][0] ]+ instructions.INSTRUCTION_TABLE_REVERSE[ all_tokens['operation'] ]['opcode']
                            print( instr[0:32] + "  tam:"+ str(len(instr[0:32]))  )

                    elif (instructions.INSTRUCTION_TABLE_REVERSE[ all_tokens['operation'] ]['type'] == "s" ):
                        #    imm[11:5] rs2 rs1 funct3 imm[4:0] opcode S-type
                        print("____instrucao tipo s____")
                    elif (instructions.INSTRUCTION_TABLE_REVERSE[ all_tokens['operation'] ]['type'] == "u" ):
                        #    imm[31:12] rd opcode U-type
                        print("____instrucao tipo u____")
                    elif (instructions.INSTRUCTION_TABLE_REVERSE[ all_tokens['operation'] ]['type'] == "sb" ):
                        print("____instrucao tipo sb____")
                    elif (instructions.INSTRUCTION_TABLE_REVERSE[ all_tokens['operation'] ]['type'] == "uj" ):
                        print("____instrucao tipo uj____")
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

            else: # se nao tiver instrucao, procura em diretivas
                if all_tokens['operation'] in DIRECTIVES_TABLE: 
                    pass
                    #DIRECTIVES_TABLE[all_tokens['operation']]
                    #contador_pos = x
                else: # senao existe instrucao nem diretiva lanca erro
                    print("Error: Operation "+ str(all_tokens['operation']) + " not recognized. Line:"+str(contador_linha)  )
                    return 2
            contador_linha = contador_linha + 1


    return 0;


#print(code)
#print("\n")
def assemble(code):
    print("Primeira Passsagem\n")
    fp_ret = first_pass(code)
    print("\n")

    if fp_ret == 0 :

        #print(SYMBOL_TABLE)
        print("------  Segunda Passsagem\n")
        sp_ret = second_pass(code)

        #print( "!!!!! ----- print teste " )
        #print(  instructions.INSTRUCTION_TABLE_REVERSE['addi']['operands']  )

    #print(scanner(processed_code))
