#Methods to build matrices
#See details in README.txt

#Method to find alignment score in a space-efficient way, two-lined matrix
def two_lined_matrix(v, w, match, mismatch, gap_open, gap_extend):
	#create two-lined matrices
	print "in two_lined_matrix"
	matrix = [[0 for i in range(len(w)+1 )] for j in range(2)]
	maxim = 0
	#matrices for deletion and insertion (affine gap penalties)
	D = [[0 for i in range(len(w)+1)] for j in range(2)]
	I = [[0 for i in range(len(w)+1)] for j in range(2)]

	#fill in two lined-matrices; updating every time i is increased
	for i in range(1, len(v)+1):
		for j in range(1, len(w)+1): 
			#line of matrix to be used
			i1 = i % 2
			i2 = (i-1) % 2

			#keep track of possible deletions
			d1 = D[i2][j] + gap_extend
			d2 = matrix[i2][j] + gap_open + gap_extend
			D[i1][j] = max(d1, d2)

			#keeping track of possible insertions
			l1 = I[i1][j-1] + gap_extend
			l2 = matrix[i1][j-1] + gap_open + gap_extend
			I[i1][j] = max(l1, l2)
			
			#check for match vs mismatch
			addition = match
			if v[i-1] != w[j-1]:
				addition = mismatch
			
			diag = matrix[i2][j-1] + addition

			#choose best score, 0 if negative because loca alignment
			if max(D[i1][j], I[i1][j] , diag) > 0:
				matrix[i1][j] = max(D[i1][j], I[i1][j], diag)
			else:
				matrix[i1][j] = 0

			#keep track of highest score and i,j positions
			if matrix[i1][j] > maxim:
				maxim = matrix[i1][j]
				loci = i
				locj = j
	return maxim, loci, locj


#Method to find alignment and score using full matrix
def full_matrix(w, v, match, mismatch, gap_open, gap_extend):
	#create the smaller matrix for scoring/alignment
	matrix2 = [[[0, '-'] for i in range(len(w)+1)] for j in range(len(v)+1)]
	D2 = [[0 for i in range(len(w)+1)] for j in range(len(v)+1)]
	I2 = [[0 for i in range(len(w)+1)] for j in range(len(v)+1)]

	#create scoring/alignment matrix
	for i in range(1, len(v)+1):
		for j in range(1, len(w)+1):

			#keep track of possible deletions
			d1 = D2[i-1][j] + gap_extend
			d2 = matrix2[i-1][j][0] + gap_open + gap_extend
			D2[i][j] = max(d1, d2)

			#keep track of possible insertions
			i1 = I2[i][j-1] + gap_extend
			i2 = matrix2[i][j-1][0] + gap_open + gap_extend
			I2[i][j] = max(i1, i2)

			#check for match/mismatch score
			addition = match
			if v[i-1] != w[j-1]:
				addition = mismatch
			diag = matrix2[i-1][j-1][0] + addition

			#determine highest score
			if max(D2[i][j], I2[i][j] , diag) > 0:
				matrix2[i][j][0] = max(D2[i][j], I2[i][j], diag)
			else:
				matrix2[i][j][0] = 0

			#fill in the hints for back tracking alignment (part C)
			if matrix2[i][j][0] == D2[i][j]:
				matrix2[i][j][1] = '^'
			if matrix2[i][j][0] == I2[i][j]:
				matrix2[i][j][1] = '<'
			if matrix2[i][j][0] == diag:
				matrix2[i][j][1] = '/'

	#Find position of local max
	loci = 0
	locj = 0
	maxim = 0
	for i in range(1, len(v)+1):
		for j in range(1, len(w)+1):
			if matrix2[i][j][0] > maxim:
				maxim = matrix2[i][j][0]
				loci = i
				locj = j
	return maxim, loci, locj, matrix2