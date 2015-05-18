###You are given an n x n 2D matrix representing an image.
###Rotate the image by 90 degrees (clockwise).
###Follow up:
###Could you do this in-place?


###invert and then reverse rows
#time O(n^2)
#space O(1)
def rotateimage(matrix):
	n = len(matrix)
	for i in range(n):
		for j in range(i+1,n):
			temp = matrix[i][j]
			matrix[i][j] = matrix[j][i]
			matrix[j][i] = temp
	for i in range(n):
		matrix[i].reverse
	return matrix
