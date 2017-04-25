from utils import settings

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


	print(unumb)	

def display_registers(regs=-1, mode='dec'):
	#print(registers[u2bin(regs,5)])
	print("Registers Display:")
	print("#################################################################")
	if(regs==-1):
		for i in range(0,32):
			if mode == 'dec':
				print("# - Reg"+str(i)+"\t=\t"+str(bin2s(settings.registers[u2bin(i,5)]))+"\t")
			elif mode == 'bin':
				print("# - Reg"+str(i)+"\t=\t"+str(settings.registers[u2bin(i,5)])+"\t#")
	else:
		print("# - Reg"+str(regs)+"\t=\t"+str(bin2s(settings.registers[u2bin(regs,5)]))+"\t")
	print("#################################################################")

def display_memory(intval_strt=0, intval_end=settings.DATA_MEMORY_SIZE):

	print("Memory Display:")
	print("#################################")
	for i in range(intval_strt, intval_end):
		print("# - Addr"+str(i)+"\t=\t"+str(settings.data_memory[i])+"\t#")

	print("#################################")