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

settings.registers[settings.rs1] = '00000000000000000001000000011100'
settings.registers[settings.rs2] = '00000000000000000000000000000011'
#settings.registers[settings.rd] = '00000000000000000000000000000011'

instructions.instr_sll()
print(settings.registers[settings.rd])

instructions.instr_srl()
print(settings.registers[settings.rd])

instructions.instr_sra()
print(settings.registers[settings.rd])