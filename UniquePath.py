 ###A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
###The robot can only move either down or right at any point in time. The robot is trying to reach 
###the bottom-right corner of the grid (marked 'Finish' in the diagram below).
###How many possible unique paths are there?
 
 # time O(m*n)
 #space O(m*n)
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

#time O(m*n)
#space O(m+n)
class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        if m < n:
            return self.uniquePaths(n, m)
        ways = [1] * n
        
        for i in xrange(1, m):
            for j in xrange(1, n):
                ways[j] += ways[j - 1]
        
        return ways[n - 1]

if __name__ == "__main__":
    print Solution().uniquePaths(1, 2)
