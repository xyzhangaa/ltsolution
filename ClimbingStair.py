###You are climbing a stair case. It takes n steps to reach to the top.

###Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

def ClimbingStair(n):
	dp = [1 for _ in range(n+1)]
	for i in range(2,n+1):
		dp[i] = dp[i-1]+dp[i-2]
	return dp[n]
