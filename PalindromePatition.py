###Given a string s, partition s such that every substring of the partition is a palindrome.

###Return all possible palindrome partitioning of s.

###For example, given s = "aab",
###Return

###  [
###    ["aa","b"],
###    ["a","a","b"]
###  ]

#O(n^2), O(n^2)
class Solution:
	def isPalindrom(self,s):
		for i in range(len(s)):
			if s[i] != s[-i-1]:
				return False
		return True
	def dfs(self,s,stringlist):
		if len(s) == 0:
			result.append(stringlist)
		for i in range(1,len(s)+1):
			if self.isPalindromw(s[:i]):
				self.dfs(s[i:],stringlist+[s[:i]])
	def PalindromePatition(s):
		result = []
		self.dfs(s,[],res)
		return result
