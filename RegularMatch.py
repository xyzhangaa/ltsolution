###Implement regular expression matching with support for '.' and '*'.

###'.' Matches any single character.
###'*' Matches zero or more of the preceding element.

###The matching should cover the entire input string (not partial).

###The function prototype should be: bool isMatch(const char *s, const char *p)

###Some examples:
###isMatch("aa","a") → false
###isMatch("aa","aa") → true
###isMatch("aaa","aa") → false
###isMatch("aa", "a*") → true
###isMatch("aa", ".*") → true
###isMatch("ab", ".*") → true
###isMatch("aab", "c*a*b") → true

### Recursive LTE
def RegularMatch(s,t):
	if len(t) == 0:
		return len(s) == 0
	if len(t) == 1 or t[1] != '*':
		if len(s) == 0 or (s[0] != t[0] and t[0] != '.'):
			return False
		return RegularMatch(s[1:],t[1:])
	else:
		i = -1
		length = len(s)
		while i < length and (i<0 or t[0]=='.' or t[0] == s[i]):
			if RegularMatch(s[i+1:],t[2:]):
				return True
			i+=1
		return False
		
### DP
def RegularMatchDP(s,t):
	dp = [[False for _ in range(len(t)+1)] for _ in range(len(s)+1)]
	dp[0][0] = True
	for i in range(1,len(t)+1):
		if t[i-1] == '*':
			if i >= 2:
				dp[0][i] = dp[0][i-2]
	for i in range(1,len(s)+1):
		for j in range(1,len(t)+1):
			if t[j-1] == '.':
				dp[i][j]=dp[i-1][j-1]
			elif t[j-1] =='*':
				dp[i][j] = dp[i][j-1] or dp[i][j-2] or (dp[i-1][j] and (s[i-1] == t[j-2] or t[j-2] == '.'))
			else:
				dp[i][j] = dp[i-1][j-1] and s[i-1] == t[j-1]
	return dp[len(s)][len(t)]
