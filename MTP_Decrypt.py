#  Coursera Cryptography Week Programming Assignment

import binascii

def readText(input):
	file = open(input, 'r')
	i = 0; inputlist = []
	for line in file:
  		if i == 1:
    			inputlist.append(line)
    			i = i - 1
		if line[0:10] == 'ciphertext':
    			print line
    			i = i + 1
    			
def ConvertBinary(text):
	scale = 16 ## equals to hexadecimal
	num_of_bits = 8
	output = bin(int(text, scale))[2:].zfill(num_of_bits)
	print output
	print type(output)

	
def XOR(binarystr1,binarystr2):
	n = 0; binarystr1 = ''; binarystr2 = ''
	output = ''
	while n <= len(binarystr1) and len(binarystr1) == len(binarystr2):
		if binarystr1[n] != binarystr2[n] == 'True':
			output = output + '1'
		else:
			output = output + '0'
		n = n + 1
	print output
	
def main():
	#XOR('1000','0001')
	print 'Complete'
	
	
	
if __name__ == "__main__": main()


print hex(0x.... ^ 0x...)