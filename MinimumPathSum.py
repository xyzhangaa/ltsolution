###Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes 
###the sum of all numbers along its path.
###Note: You can only move either down or right at any point in time.

def minpathsum(grid):
  row = len(grid)
  col = len(grid[0])
  A = [[0 for _ in range(col)] for _ in range(row)]
  A[0][0] = grid[0][0]
  for i in range(1,col):
    A[0][i] = grid[0][i] + A[0][i-1]
  for i in range(1,row):
    A[i][0] = A[i-1][0] + grid[i][0]
  for i in range(1,row):
    for j in range(1,col):
      A[i][j] = min(grid[i-1,j],grid[i,j-1])+grid[i][j]
  return A[row-1][col-1]
  
