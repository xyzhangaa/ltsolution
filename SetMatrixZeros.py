###Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.
#time O(m*n)
#space O(m+n)

def setmatrixzeros(matrix):
	nrow = len(matrix)
	ncol = len(matrix[0])
	row = [False for _ in range(nrow)]
	col = [False for _ in range(ncol)]
	for i in range(nrow):
		for j in range(ncol):
			if matrix[i][j]==0:
				row[i] = True
				col[j] = True
	for i in range(nrow):
		for j in range(ncol):
			if row[i] or col[j]:
				matrix[i][j] = 0
	
