###Follow up for "Unique Paths":

###Now consider if some obstacles are added to the grids. How many unique paths would there be?

###An obstacle and empty space is marked as 1 and 0 respectively in the grid.



def UniquePathtwo(grid):
	m = len(grid)
	n = len(grid[0])
	path = [[0 for _ in range(n)] for _ in range(m)]
	for i in range(m):
		if grid[i][0] == 0:
			path[i][0] = 1
		else:
			path[i][0] = 1
			break
	for i in range(n):
		if grid[0][i] == 0:
			path[0][i] = 1
		else:
			path[i][0] = 0
			break
	for i in range(1,m):
		for j in range(1,n):
			if grid[i][j] == 1:
				path[i][j] = 0
			else:
				path[i][j] = path[i-1][j]+path[i][j-1]
	return path[m-1][n-1]
