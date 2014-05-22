#Script to perform local alignment in a space efficent way on two 
#long sequences. Returns the score of the alignment, length of the
#sequences, and the actual alignment
#For details, see README.txt

import sys
import alignment 
import build_matrix

#method to find local alignment
def loc_align(str1, str2, match, mismatch, gap_open, gap_extend):

	#find the maximum length of best local alignment, no back-tracking
	maxim, loci, locj = build_matrix.two_lined_matrix(str1, str2, match, mismatch, 
		gap_open, gap_extend)	
				
	#output best score
	print "Score: " + str(maxim)
	return maxim

	#reduce to substrings, chose minimum to work with scoring choices
	if (locj - (maxim*(abs(mismatch)+1))) > 0:
		startj = (locj - (maxim*(abs(mismatch)+1)))
	else:
		startj = 0

	if (loci - (maxim*(abs(mismatch)+1))) > 0:
		starti = (loci - (maxim*(abs(mismatch)+1)))
	else:
		starti = 0

	w = w[startj:-(len(w)-locj - 1)]
	v = v[starti:-(len(v)-loci - 1)]


	#create a smaller matrix with back-tracing	
	maxim, loci, locj, matrix2 = build_matrix.full_matrix(v, w, match,
	 mismatch, gap_open, gap_extend)

	#initialize alignment sequences
	str1, str2 = "", ""

	#Find Alignment
	str1, str2 = alignment.find_alignment(matrix2, loci, locj, str1, 
		str2, v, w)

	#print length of alignment
	print "length: " + str(len(str1)) + '\n'

	#print alignment
	alignment.print_alignment(str1, str2)


