###Given an integer n, generate a square matrix filled with elements from 1 to n^2 in spiral order.
###For example,
###Given n = 3,

###You should return the following matrix:
###[
### [ 1, 2, 3 ],
### [ 8, 9, 4 ],
### [ 7, 6, 5 ]
###]

def SpiralMatrixTwo(n):
	if n == 0:
		return []
	matrix = [[0 for _ in range(n)] for _ in range(n)]
	up = 0
	left = 0
	right = n-1
	down = n-1
	direc = 0
	count = 0
	while True:
		if direc == 0:
			for i in range(left,right+1):
				count += 1
				matrix[up][i] = count
			up += 1
		if direc == 1:
			for i in range(up,down+1):
				count += 1
				matrix[i][right] = count
			right -= 1
		if direc == 2:
			for i in range(right,left-1,-1):
				count += 1
				matrix[down][i] = count
			down -= 1
		if direc == 3:
			for i in range(down,up-1,-1):
				count += 1
				matrix[i][left] = count
			left += 1
		if count == n*n:
			return matrix
		direc = (direc+1)%4
