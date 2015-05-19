###Given a string S and a string T, count the number of distinct subsequences of T in S.

###A subsequence of a string is a new string which is formed from the original string by 
###deleting some (can be none) of the characters without disturbing the relative positions 
###of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

###Here is an example:
###S = "rabbbit", T = "rabbit"
###Return 3.

def distinctsub(s,t):
	if len(s) < len(t):
		return False
	dp = [[0 for _ in range(len(t)+1)] for _ in range(len(s)+1)]
	for j in range(len(s)+1):
		dp[j][0]=1
	for i in range(1,len(s)+1):
		for j in range(1,min(i+1,len(t)+1)):
			if s[i-1] == t[j-1]:
				dp[i][j] = dp[i-1][j]+dp[i-1][j-1]
			else:
				dp[i][j] = dp[i-1][j]
	return dp[len(s)][len(t)]

# Time:  O(n^2)
# Space: O(n)
class Solution:
    # @return an integer
    def numDistinct(self, S, T):
        ways = [0 for _ in xrange(len(T) + 1)]
        ways[0] = 1
        for S_char in S:
            for j, T_char in reversed(list(enumerate(T))):
                if S_char == T_char:
                    ways[j + 1] += ways[j]
        return ways[len(T)]
        
if __name__ == "__main__":
    S = "rabbbit"
    T = "rabbit"
    result = Solution().numDistinct(S, T)
    print result
