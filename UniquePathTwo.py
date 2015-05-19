###Follow up for "Unique Paths":

###Now consider if some obstacles are added to the grids. How many unique paths would there be?

###An obstacle and empty space is marked as 1 and 0 respectively in the grid.

#time O(m*n)
#space O(m*n)
class Solution:
    # @param {integer[][]} obstacleGrid
    # @return {integer}
    def uniquePathsWithObstacles(self, obstacleGrid):
         m = len(obstacleGrid); n=len(obstacleGrid[0])
         dp = [[0 for _ in range(n)] for _ in range(m)]
         if obstacleGrid[0][0] == 1:
             return 0
         dp[0][0] = 1
         for i in range(1,m):
             if obstacleGrid[i][0] == 1:
                 dp[i][0] = 0
                 break
             else:
                 dp[i][0] = 1
         for i in range(1,n):
             if obstacleGrid[0][i] == 1:
                 dp[0][i] = 0
                 break
             else:
                 dp[0][i] = 1
         for i in range(1,m):
             for j in range(1,n):
                 if obstacleGrid[i][j] == 1:
                     dp[i][j] = 0
                 else:
                     dp[i][j] = dp[i-1][j]+dp[i][j-1]
         return dp[m-1][n-1]

class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        ways = [0] * n
        
        if obstacleGrid[0][0] == 0:
            ways[0] = 1
            
        for j in xrange(1, n):
            if obstacleGrid[0][j] == 1:
                ways[j] = 0
            else:
                ways[j] = ways[j - 1]
        
        for i in xrange(1, m):
            if obstacleGrid[i][0] == 1:
                ways[0] = 0
                
            for j in xrange(1, n):
                if obstacleGrid[i][j] == 1:
                    ways[j] = 0
                else:
                    ways[j] += ways[j - 1]
        
        return ways[n - 1]

if __name__ == "__main__":
    obstacleGrid = [
                      [0,0,0],
                      [0,1,0],
                      [0,0,0]
                   ]
    print Solution().uniquePathsWithObstacles(obstacleGrid)
