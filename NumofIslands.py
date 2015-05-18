# Time:  O(m * n)
# Space: O(m * n)

#Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

#BFS
class Solution:
  def numislands(self,grid):
    ans = 0
    if not len(grid):
      return ans
    m,n = len(grid), len(grid[0])
    visited = [[False]*n for _ in range(m)]
    for x in range(m):
      for y in range(n):
        if grid[x][y] == '1' and not visited[x][y]:
          ans += 1
          self.bfs(grid,visited,x,y,m,n)
    return ans
  
  def bfs(self,grid,visited,x,y,m,n):
    dz = zip([1,0,-1,0],[0,1,0,-1])
    queue = [(x,y)]
    visited[x][y] = True
    while queue:
      front = queue.pop(0)
      for p in dz:
        np = (front[0] + p[0],front[1]+p[1])
        if self.isValid(np,m,n) and grid[np[0]][np[1]] == '1' and not visited[np[0]][np[1]]:
          visited[np[0]][np[1]] = True
          queue.append(np)
  def isValid(self,np,m,n):
    return np[0] >= 0 and np[0] < m and np[1] >=0 and np[1] < n

#DFS    
class Solution2:
  def numislands(self,grid):
    if grid == []:
      return 0
    m,n = len(grid), len(grid[0])
    visited = [[False]*n for _ in range(m)]
    count = 0
    for i in xrange(m):
      for j in xrange(n):
        if grid[i][j] == '1' and not visited[i][j]:
          self.dfs(grid,visited,m,n,i,j)
          count += 1
    return count
    
  def dfs(self,grid,visited,m,n,x,y):
    if grid[x][y] == '0' or visited[x][y]:
      return 0
    visited[x][y] = True
    
    if x != 0:
      self.dfs(grid,visited,m,n,x-1,y)
    if x != m-1:
      self.dfs(grid,visited,m,n,x+1,y)
    if y != 0:
      self.dfs(grid,visited,m,n,x,y-1)
    if y != n-1:
      self.dfs(grid,visited,m,n,x,y+1)
  
