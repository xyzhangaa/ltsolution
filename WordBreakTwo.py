###Given a string s and a dictionary of words dict, add spaces in s to construct a sentence 
###where each word is a valid dictionary word.

###Return all such possible sentences.

###For example, given
###s = "catsanddog",
###dict = ["cat", "cats", "and", "sand", "dog"].

###A solution is ["cats and dog", "cat sand dog"].

#O(n^2),O(n)
class Solution:
  def check(s,diction):
	  dp = [False for _ in range(len(s)+1)]
	  dp[0] = True
	  for i in range(1,len(s)+1):
		  for k in range(i):
		  	if dp[k] and s[k:i] in diction:
			  	dp[i] = True
  	return dp[len(s)]

  def dfs(s,diction,stringlist):
	  if check(s,dict):
		  if len(s) == 0:
		  	Solution.result.append(stringlist[1:])
		  for i in range(1,len(s)+1):
			  if s[:i] in diction:
			  	dfs(s[:i],diction,stringlist+' '+s[:i])
				
  def WordBreakTwo(s,diction):
  	Solution.result = []
	  dfs(s,diction,'')
  	return result
