###Given a string s, partition s such that every substring of the partition is a palindrome.

###Return all possible palindrome partitioning of s.

###For example, given s = "aab",
###Return

###  [
###    ["aa","b"],
###    ["a","a","b"]
###  ]

class Solution:
	def isPalindrom(s):
		for i in range(len(s)):
			if s[i] != s[-i-1]:
				return False
		return True
	def dfs(s,stringlist):
		if len(s) == 0:
			Solution.result.append(stringlist)
		for i in range(1,len(s)+1):
			if isPalindromw(s[:i]):
				dfs(s[i:],stringlist+[s[:i]])
	def PalindromePatition(s):
		Solution.result = []
		dfs(s,'')
		return Solution.result
