#Methods to align two sequences
#See details in README.txt

#Method to print alignments clearly from two strings
def print_alignment(str1, str2):
	x = 0
	y = 80
	#print in lines of 80 so alignment is clear
	while x < len(str1):
		if y > len(str1):
			print str1[x:]
			print str2[x:] + '\n'
		else:
			print str1[x:-(len(str1)-y)]
			print str2[x:-(len(str2)-y)] + '\n'
		x += 80
		y += 80

#Method to backtrace to find alignment from matrix
def find_alignment(matrix2, loci, locj, str1, str2, v, w):
	while (matrix2[loci][locj][1] != '-'):
		#indel
		if matrix2[loci][locj][1] == '^':
			loci = loci - 1
			str1 = str1 + v[loci]
			str2 = str2 + '-'
		#indel
		elif matrix2[loci][locj][1] == '<':
			locj = locj - 1
			str1 = str1 + '-'
			str2 = str2 + w[locj]
		#match or mismatch
		else:
			loci = loci - 1
			locj = locj - 1
			str1 = str1 + w[locj]
			str2 = str2 + v[loci]
	return str1, str2
