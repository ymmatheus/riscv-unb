from utils import settings

hex_table = {
	"0000":"0",
	"0001":"1",
	"0010":"2",
	"0011":"3",
	"0100":"4",
	"0101":"5",
	"0110":"6",
	"0111":"7",
	"1000":"8",
	"1001":"9",
	"1010":"a",
	"1011":"b",
	"1100":"c",
	"1101":"d",
	"1110":"e",
	"1111":"f"
}

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