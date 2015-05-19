###Given two words word1 and word2, find the minimum number of steps required 
###to convert word1 to word2. (each operation is counted as 1 step.)

###You have the following 3 operations permitted on a word:

###a) Insert a character
###b) Delete a character
###c) Replace a character

#time O(m*n)
#space O(m*n)
###Recursively
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

#time O(m*n)
#space O(m+n)
###Iteratively
class Solution:
	def editdistance(self,word1,word2):
		if len(word1) < len(word2):
			return self.editdistance(word2,word1)
		distance = [i for i in range(len(word2)+1)]
		for i in range(1,len(word1)+1):
			pre_distance_i_j = distance[0]
			distance[0] = i
			for j in range(1,len(word2)+1):
				insert = distance[j-1]+1
				delete = distance[j]+1
				replace = pre_distance_i_j
				if word1[i-1] != word2[j-1]:
					replace += 1
				pre_distance_i_j = distance[j]
				distance[j] = min(insert,delete,replace)
		return distance[-1]
