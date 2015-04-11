###Given an array of non-negative integers, you are initially positioned at the first index of the array.

###Each element in the array represents your maximum jump length at that position.

###Your goal is to reach the last index in the minimum number of jumps.

###For example:
###Given array A = [2,3,1,1,4]

###The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)

###Brute Force time O(n^2)
def JumpGameII(A):
	maxint = 1<<31-1
	dp = [maxint for _ in range(len(A))]
	dp[0] = 0
	for i in range(1,len(A)):
		for j in range(i):
			if A[j] >= i-j:
				dp[i] = min(dp[i],dp[j]+1)
	return dp[-1]

###tricky solution
### last represents the maximum distance reached by a minimum ret steps; curr represents the maximum distance reached by a ret+1 steps

def JumpGameTwo(A):
	step = 0
	curr = 0
	last = 0
	for i in range(len(A)):
		if i > last:
			last = curr
			step += 1
		curr = max(curr, i+A[i])
	return step
