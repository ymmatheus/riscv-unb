from utils import settings, instructions, utilities
from simulator import simulator

settings.opcode = ''
settings.rd = '00000000000000000000000000000100'
settings.funct3 = ''
settings.rs1 = '00000000000000000000000000000010'
settings.rs2 = '00000000000000000000000000000011'
settings.funct7 = ''
settings.imm_i = ''
settings.imm_s = ''
settings.imm_b = ''
settings.imm_u = ''
settings.imm_j = ''
settings.shamnt = ''

settings.registers[settings.rs1] = '00000000000000000000000000000000'
settings.registers[settings.rs2] = '00000000000000000000000000000111'
settings.imm_i = '00000000000000000000000000000101'
settings.data_memory[0] = "00110100"
settings.data_memory[1] = "00000110"
settings.data_memory[2] = "11101100"
settings.data_memory[3] = "00110101"
settings.data_memory[4] = "10001100"
settings.data_memory[5] = "10110000"

instructions.instr_lw()
print(settings.registers[settings.rd])