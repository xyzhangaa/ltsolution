 ###A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
###The robot can only move either down or right at any point in time. The robot is trying to reach 
###the bottom-right corner of the grid (marked 'Finish' in the diagram below).
###How many possible unique paths are there?
 
 
 def UniquePath(m,n):
	if m == 1 or n ==1:
		return 1
	else:
		path = [[0 for _ in range(n)] for _ in range(m)]
		for i in range(m):
			path[i][0] = 1
		for i in range(n):
			path[0][i] = 1
		for i in range(1,m):
			for j in range(1,n):
				path[i][j] = path[i-1][j]+path[i][j-1]
		return path[m-1][n-1]
