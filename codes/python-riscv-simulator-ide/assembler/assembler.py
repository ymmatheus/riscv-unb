
DIRECTIVES_TABLE = [ ".data" , ".text" , ".space" , ".word" , ".ascii" , ".asciiz", ".byte" ]

SYMBOL_TABLE = {}


REGISTER_NAMES = [
    "x0", "x1", "x2", "x3", "x4", "x5", "x6", "x7", "x8", "x9", "x10", "x11", "x12", "x13", "x14", "x15", "x16",
    "x17", "x18", "x19", "x20", "x21", "x22", "x23", "x24", "x25", "x26", "x27", "x28", "x29", "x30", "x31", "zero",
    "ra", "sp", "gp", "tp", "t0", "t1", "t2", "fp", "s0", "s1", "a0", "a1", "a2", "a3", "a4", "a5", "a6", "a7",
    "s2", "s3", "s4", "s5", "s6", "s7", "s8", "s9", "s10", "s11", "t3", "t4", "t5", "t6",
]

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




def first_pass(code_text):

    contador_pos = 0
    contador_linha = 1

    # To lower case
    code_text = code_text.lower()
    # Separa por linhas
    code_text = code_text.split("\n")


    code_text_aux = list()
    for line in code_text:

        all_tokens = split_tokens(line, contador_linha)
        print(line)
        print(all_tokens)
        print("")
        if all_tokens['label'] != '':
            # procura label na tabela de simbolos
            if all_tokens['label'] in SYMBOL_TABLE:
                # simbolo redefinido
                print("Error: Duplicated Symbol")
                return 1
            else:
                # insere rotulo e contador_posicao na tablea de simbolos
                SYMBOL_TABLE[ all_tokens['label'] ] = contador_pos;

            # procura operacao na taela de instrucoes
            if all_tokens['operation'] in INSTRUCTION_TABLE:
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

def second_pass(code_text):

    contador_pos = 0
    contador_linha = 1

    # To lower case
    code_text = code_text.lower()
    # Separa por linhas
    code_text = code_text.split("\n")


    code_text_aux = list()
    for line in code_text:

        all_tokens = split_tokens(line, contador_linha)
        print(line)
        print(all_tokens)
        print("")
        if all_tokens['label'] != '':
            # procura label na tabela de simbolos
            if all_tokens['label'] in SYMBOL_TABLE:
                # simbolo redefinido
                print("Error: Duplicated Symbol")
                return 1
            else:
                # insere rotulo e contador_posicao na tablea de simbolos
                SYMBOL_TABLE[ all_tokens['label'] ] = contador_pos;

            # procura operacao na taela de instrucoes
            if all_tokens['operation'] in INSTRUCTION_TABLE:
                contador_pos = contador_pos + INSTRUCTION_TABLE[ all_tokens['operation'] ]
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






code = '''ADDI x1, zero, 56
ADDI $t1, $t0, 44
label1:ADDI $t1, $t0, 441
ADDI  $t1 , $t0, 442
;comentaario
label2:ADDI $t1, $t0,  443

label3:ADD $t2, $t1, $t0

ADDI $t1, $t0, 44 ; comments
ADDI  $t1 , $t0, 444  

ADDI $t1, $t0, 445
ADDI $t1, $t0, 446 
ADDI $t1, $t0, 44'''



fp_ret = first_pass(code)

if fp_ret == 0 :
    print(SYMBOL_TABLE)

#print(scanner(processed_code))
