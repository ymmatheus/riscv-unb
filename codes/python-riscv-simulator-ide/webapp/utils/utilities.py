# -*- coding: utf-8 -*-
'''

	TODO:
		- limitar conversões para 64 bits


'''


from utils import settings

hex_table = {
	"0000":"0",	"0001":"1",	"0010":"2",	"0011":"3",	"0100":"4",	"0101":"5",	"0110":"6",	"0111":"7",	"1000":"8",	"1001":"9",
	"1010":"a",	"1011":"b",	"1100":"c",	"1101":"d",	"1110":"e",	"1111":"f",	"0":"0000",	"1":"0001",	"2":"0010",	"3":"0011",
	"4":"0100",	"5":"0101",	"6":"0110",	"7":"0111",	"8":"1000",	"9":"1001",	"a":"1010",	"b":"1011",	"c":"1100",	"d":"1101",
	"e":"1110",	"f":"1111"	
}

class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\x1b[0;31;40m'
	ENDC = '\x1b[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'

'''Checa se string e um numero inteiro hex ou bin'''
def is_number(s):
	s = s.strip()
	n_prefix = s[0:2]

	hex_digits = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
	bin_digits = ['0', '1']

	if(n_prefix == "0x"):
		for c in s[2:]:
			if c.lower() not in hex_digits:
				return False

		return True
	elif( n_prefix == "0b" ):
		for c in s[2:]:
			if c not in bin_digits:
				return False
		return True
	else:
		try:
			int(s)
			return True
		except ValueError:
			return False

def get_immediate(v, symbol_table, imm_len):

	if( is_number(v) ):
		pass
		#return num em binario
	else:
		pass
		#senao checa se v eh label

# Negate Binary
def neg_bin(bin_code):
	bin_code_len = len(bin_code)
	bin_code_neg = ['' for i in range(bin_code_len)]

	for i in range(0,bin_code_len):
		
		if bin_code[i] == '1':
			bin_code_neg[i] = '0'
		elif bin_code[i] == '0':
			bin_code_neg[i] = '1'
		else:
			print("neg_bin_error: value different than 0 or 1")
			bin_code_neg[i] = 'x'

	return ''.join(bin_code_neg)

# Unsigned to Binary
def u2bin(unumb,xlen):
	binstr = ""
	while(unumb>1):
		rmindr = unumb%2
		unumb = unumb//2
		binstr += str(rmindr)
		#print(unumb)
	binstr += str(unumb)

	return(binstr[::-1].zfill(xlen))

# Binary to Unsigned
def bin2u(binnumb):
	lennumb = len(binnumb)-1
	unumb = 0
	for i in range(0,len(binnumb)):
		unumb = unumb + 2**lennumb * int(binnumb[i]) 
		#print(binnumb[i])
		lennumb = lennumb-1
	return unumb

# Binary to Signed
def bin2s(binnumb):
	snumb = bin2u(binnumb)
	if(binnumb[0] == '1'):
		return snumb - 2**len(binnumb)
	return snumb

# Signed to Binary
def s2bin(snumb,xlen):
	'''
		todo: handle xlen too small for right representation
			s2bin(4,3) can't be represented on 2's complement
	'''
	pos_snumb = snumb*-1
	
	if snumb>=0 :
		pos_sbin = u2bin(snumb,xlen)
		return pos_sbin 
	else:
		pos_sbin = u2bin(pos_snumb,xlen)
		pos_sbin_neg = neg_bin(pos_sbin)
		return u2bin(bin2u(pos_sbin_neg)+1 , xlen) 
	

def bin2hex(binnumb):
	hexnumb = ''
	if len(binnumb) % 4 == 0 :
		for i in range(0,len(binnumb)//4):
			#print(binnumb[i*4 : (i+1)*4])
			hexnumb = hexnumb + hex_table[binnumb[i*4 : (i+1)*4]]
	return hexnumb


def bin_soma(num1, num2):
	n_digits_n1 = len(num1)
	n_digits_n2 = len(num2)
	n_digits_max = max([ n_digits_n1 , n_digits_n2 ])
	num1 = ''.zfill(n_digits_max - n_digits_n1)+num1
	num2 = ''.zfill(n_digits_max - n_digits_n2)+num2
	#print(num1)
	#print(num2)
	soma = ["0" for i in range(0,n_digits_max)]	
	carry = "0"
	for i in range( -1, -n_digits_max-1 , -1):
		if num1[i]=="0" and num2[i]=="0" and carry=="0" :
			soma[i] = "0"
			#carry=0
		elif num1[i]=="1" and num2[i]=="1" and carry=="1" :
			soma[i] = "1"
			carry = "1"
		else:
			if (carry == "1" and num1[i]=="1") or (carry == "1" and num2[i]=="1") or (num1[i] == "1" and num2[i]=="1"):
				soma[i]="0"
				carry="1"
			else:
				soma[i]="1"
				carry="0"

	return ''.join(soma)


def display_registers(regs=-1, mode='dec'):
	#print(registers[u2bin(regs,5)])
	print("Registers Display:")
	print("#################################################################")
	if(regs==-1):
		for i in range(0,32):
			if mode == 'dec':
				print("# - Reg"+str(i)+"\t=\t"+str(bin2s(settings.registers[u2bin(i,5)]))+"\t")
			elif mode == 'bin':
				print("# - Reg"+str(i)+"\t=\t"+str(settings.registers[u2bin(i,5)])+"\t")
			else:
				print("# - Reg"+str(i)+"\t=\t0x"+str(bin2hex(settings.registers[u2bin(i,5)]))+"\t")
	else:
		if mode == 'dec':
			print("# - Reg"+str(regs)+"\t=\t"+str(bin2s(settings.registers[u2bin(i,5)]))+"\t")
		elif mode == 'bin':
			print("# - Reg"+str(regs)+"\t=\t"+str(settings.registers[u2bin(i,5)])+"\t")
		else:
			print("# - Reg"+str(regs)+"\t=\t0x"+str(bin2hex(settings.registers[u2bin(i,5)]))+"\t")
	print("#################################################################")



def display_memory(intval_strt=0, intval_end=settings.DATA_MEMORY_SIZE, mode='hex'):
	print("Memory Display:")
	print("#################################################################")
	for i in range(intval_strt, intval_end):
		if mode == 'dec':
			print("# - Addr"+str(i)+"\t=\t"+str( bin2s( settings.data_memory[i] ))+"\t")			
		elif mode == 'bin':			
			print("# - Addr"+str(i)+"\t=\t"+str( settings.data_memory[i] )+"\t")
		else:
			print("# - Addr"+str(i)+"\t=\t0x"+str( bin2hex( settings.data_memory[i] ) )+"\t")
	print("#################################################################")


def display_codeobj(objcode, display_format="hex"):

	print("Codigo objeto:(bin ou hex)")
	if(display_format == "bin"):
		print("BIN")
		print("#################################################################")
		print(objcode)
		print("#################################################################")
	elif(display_format == "hex"):
		print("HEX")
		print("#################################################################")
		for i in objcode.split('\n'):
			print("0x{:08X}".format(bin2u(i)))
		print("#################################################################")

# Receives a list of binary data and convert to specified format
def dump_convert(data, dump_format="hex"):
	data_dump_list = []
	#print(data)
	if dump_format == "hex":
		for i in data:
			#data_dump_list.append(bin2hex(data[i]))
			data_dump_list.append(bin2hex(i))
	
	elif dump_format == "mif":
		numbr_of_addrs = 256
		data_dump_list.append("DEPTH="+str(numbr_of_addrs)+";")
		data_dump_list.append("")
		data_dump_list.append("ADDRESS_RADIX=UNS;")
		data_dump_list.append("DATA_RADIX=HEX;")
		data_dump_list.append("CONTENT BEGIN")
		data_dump_list.append("")

		#print mif_header
		n_rep=0
		first_rep=0

		# instructions = data
		instructions = []
		for inst in data:
			instructions.append(inst)

		#print(instructions)
		#return
		if instructions:
			last_line = bin2hex(instructions.pop(0))
		else:
			return []

		current_line=''
		zeros_pattern = "00000000"		

		cont = 1
		for i in range(1,int(numbr_of_addrs)):
			
			if instructions:
				current_line = bin2hex(instructions.pop(0))

			if current_line == '':
				current_line = zeros_pattern
			#write_file.write("\t["+str(i-1)+".."+str(i)+"]	:   "+last_line+";\n")
			#write_file.write("\t"+str(i-1)+"	:   "+last_line+";\n")
			
			if current_line != last_line :
				if n_rep == 0 :
					#write_file.write("\t"+str(i-1)+"	:   "+last_line+";\n")
					data_dump_list.append("\t"+str(i-1)+"	:   "+last_line+";")
				else:

					#write_file.write("\t["+str(first_rep)+".."+str(i)+"]	:   "+last_line+";\n")
					data_dump_list.append("\t["+str(first_rep)+".."+str(i)+"]	:   "+last_line+";")
				n_rep = 0
				first_rep = i

			else:
				n_rep = n_rep + 1
			
			

			if i == numbr_of_addrs-1:
				if n_rep == 0 :
					data_dump_list.append("\t"+str(i-1)+"	:   "+last_line+";")
					data_dump_list.append("\t"+str(i)+"	:   "+current_line+";")

					#write_file.write("\t"+str(i-1)+"	:   "+last_line+";\n")
					#write_file.write("\t"+str(i)+"	:   "+current_line+";\n")
				else:
					#write_file.write("\t["+str(first_rep)+".."+str(i)+"]	:   "+last_line+";\n")
					data_dump_list.append("\t["+str(first_rep)+".."+str(i)+"]	:   "+last_line+";")

			last_line = current_line
		data_dump_list.append("END;")
		#write_file.write("END;")

	#print(data_dump_list)
		pass
	return data_dump_list


def save_to_file(codeobj, filename="file_out",  file_format="mif"):
	
	try:
		write_file = open(filename+"."+file_format,'w')
	except:
		print("Nao foi possivel criar este arquivo!")
		sys.exit(12)
	if(file_format == "mif"):
		pass
	else:

		instructions = codeobj.split("\n")

		for instruction in instructions:
			write_file.write("{}\n".format( bin2hex(instruction) ))

