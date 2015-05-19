###Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.
###For example,
###Given:
###s1 = "aabcc",
###s2 = "dbbca",

###When s3 = "aadbbcbcac", return true.
###When s3 = "aadbbbaccc", return false.

#O(m*n), O(m*n)
def interleavestring(s1,s2,s3):
	if len(s1)+len(s2) != len(s3):
		return False
	dp = [[False for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
	dp[0][0] = True
	for i in range(1,len(s1)+1):
		dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
	for j in range(1,len(s2)+1):
		dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]
	for i in range(1,len(s1)+1):
		for j in range(1,len(s2)+1):
			dp[i][j] =(dp[i-1][j] and s1[i-1]==s3[i+j-1]) \
				   or (dp[i][j-1] and s2[j-1] == s3[i+j-1])
	return dp[len(s1)][len(s2)]

# Time:  O(m * n)
# Space: O(m + n)
# Dynamic Programming + Sliding Window
class Solution:
    # @return a boolean
    def isInterleave(self, s1, s2, s3):
        if len(s1) + len(s2) != len(s3):
            return False
        if len(s1) > len(s2):
            return self.isInterleave(s2, s1, s3)
        match = [False for i in xrange(len(s1) + 1)]
        match[0] = True
        for i in xrange(1, len(s1) + 1):
            match[i] = match[i -1] and s1[i - 1] == s3[i - 1]
        for j in xrange(1, len(s2) + 1):
            match[0] = match[0] and s2[j - 1] == s3[j - 1]
            for i in xrange(1, len(s1) + 1):
                match[i] = (match[i - 1] and s1[i - 1] == s3[i + j - 1]) \
                                       or (match[i] and s2[j - 1] == s3[i + j - 1])
        return match[-1]

# Time:  O(m * n)
# Space: O(m * n)
# Recursive + Hash  
class Solution3:
    # @return a boolean
    def isInterleave(self, s1, s2, s3):
        self.match = {}
        if len(s1) + len(s2) != len(s3):
            return False
        return self.isInterleaveRecu(s1, s2, s3, 0, 0, 0)
    
    def isInterleaveRecu(self, s1, s2, s3, a, b, c):
        if repr([a, b]) in self.match.keys():
            return self.match[repr([a, b])]
        
        if c == len(s3):
            return True
        
        result = False
        if a < len(s1) and s1[a] == s3[c]:
            result = result or self.isInterleaveRecu(s1, s2, s3, a + 1, b, c + 1)
        if b < len(s2) and s2[b] == s3[c]:
            result = result or self.isInterleaveRecu(s1, s2, s3, a, b + 1, c + 1)
            
        self.match[repr([a, b])] = result 
        
        return result

if __name__ == "__main__":
    print Solution().isInterleave("a", "", "a")
    print Solution().isInterleave("aabcc", "dbbca", "aadbbcbcac")
    print Solution().isInterleave("aabcc", "dbbca", "aadbbbaccc")
