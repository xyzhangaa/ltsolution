###Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

###For example,
###Given the following matrix:

###[
### [ 1, 2, 3 ],
### [ 4, 5, 6 ],
### [ 7, 8, 9 ]
###]
###You should return [1,2,3,6,9,8,7,4,5].


def SpiralMatrix(matrix):
	if matrix == []:
		return []
	up = 0
	left = 0
	right = len(matrix)-1
	down = len(matrix[0])-1
	direc = 0
	result = []
	while True:
		if direc == 0:
			for i in range(left,right+1):
				result.append(matrix[up][i])
			up += 1
		if direc == 1:
			for i in range(up,down+1):
				result.append(matrix[i][right])
			right -= 1
		if direc == 2:
			for i in range(right,left-1,-1):
				result.append(matrix[down][i])
			down -= 1
		if direc == 3:
			for i in range(down,up-1,-1):
				result.append(matrix[i][left])
			left += 1
		if up > down or left > right:
			return result
		direc = (direc+1)%4
