###You are climbing a stair case. It takes n steps to reach to the top.

###Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

###Recursively
#time O(n)
#space O(n)
def ClimbingStair(n):
	dp = [1 for _ in range(n+1)]
	for i in range(2,n+1):
		dp[i] = dp[i-1]+dp[i-2]
	return dp[n]

###Itervatively
#time O(n)
#space O(1)
class Solution:
	def ClimbingStair(n):
		prev,curr= 0,1
		for i in xrange(n):
			prev,curr= curr,prev+curr
		return curr
