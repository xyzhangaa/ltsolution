###Given a string s, partition s such that every substring of the partition is a palindrome.

###Return the minimum cuts needed for a palindrome partitioning of s.

###For example, given s = "aab",
###Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.

def PalindromePartitionTwo(s):
	if len(s) == 0 or len(s) == 1:
		return 0
	p = [[False for _ in range(len(s))] for _ in range(len(s))]
	dp = [0 for _ in range(len(s)+1)]
	for i in range(len(s)+1):
		dp[i] = len(s) - i
	for i in range(len(s)-1,-1,-1):
		for j in range(i,len(s)):
			if s[i] == s[j] and ((j-i) < 2 or p[i+1][j-1]):
				p[i][j] = True
				dp[i] = min(1+dp[j+1],dp[i])
	return dp[0]-1
