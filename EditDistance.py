###Given two words word1 and word2, find the minimum number of steps required 
###to convert word1 to word2. (each operation is counted as 1 step.)

###You have the following 3 operations permitted on a word:

###a) Insert a character
###b) Delete a character
###c) Replace a character

def EditDistance(s1,s2):
	dp = [[0 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
	for i in range(len(s1)+1):
		dp[i][0] = i
	for i in range(len(s2)+1):
		dp[0][i] = i
	for i in range(1,len(s1)+1):
		for j in range(1,len(s2)+1):
			if s1[i-1] == s2[j-1]:dp[i][j] = min(dp[i-1][j]+1,dp[i][j-1]+1,dp[i-1][j-1])
			else:
				dp[i][j] = min(dp[i-1][j]+1,dp[i][j-1]+1,dp[i-1][j-1]+1)
	return dp[len(s1)][len(s2)]
