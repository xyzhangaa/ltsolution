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

# Time:  O(m * n)
# Space: O(n)
# dp with rolling window
class Solution:
    # @return a boolean
    def isMatch(self, s, p):
        k = 3
        result = [[False for j in xrange(len(p) + 1)] for i in xrange(k)]
        
        result[0][0] = True
        for i in xrange(2, len(p) + 1):
            if p[i-1] == '*':
                result[0][i] = result[0][i-2]
        
        for i in xrange(1,len(s) + 1):
            if i > 1:
                result[0][0] = False
            for j in xrange(1, len(p) + 1):
                if p[j-1] != '*':
                    result[i % k][j] = result[(i-1) % k][j-1] and (s[i-1] == p[j-1] or p[j-1] == '.')
                else:
                    result[i % k][j] = result[i % k][j-2] or (result[(i-1) % k][j] and (s[i-1] == p[j-2] or p[j-2]=='.'))
                    
        return result[len(s) % k][len(p)]

# dp
# Time:  O(m * n)
# Space: O(m * n)
class Solution2:
    # @return a boolean
    def isMatch(self, s, p):
        result = [[False for j in xrange(len(p) + 1)] for i in xrange(len(s) + 1)]
        
        result[0][0] = True
        for i in xrange(2, len(p) + 1):
            if p[i-1] == '*':
                result[0][i] = result[0][i-2]
                    
        for i in xrange(1,len(s) + 1):
            for j in xrange(1, len(p) + 1):
                if p[j-1] != '*':
                    result[i][j] = result[i-1][j-1] and (s[i-1] == p[j-1] or p[j-1] == '.')
                else:
                    result[i][j] = result[i][j-2] or (result[i-1][j] and (s[i-1] == p[j-2] or p[j-2]=='.'))
                    
        return result[len(s)][len(p)]

# iteration
class Solution3:
    # @return a boolean
    def isMatch(self, s, p):
        p_ptr, s_ptr, last_s_ptr, last_p_ptr = 0, 0, -1, -1
        last_ptr = []
        while s_ptr < len(s):
            if p_ptr < len(p) and (p_ptr == len(p) - 1 or p[p_ptr + 1] != '*') and \
            (s_ptr < len(s) and (p[p_ptr] == s[s_ptr] or p[p_ptr] == '.')):
                    s_ptr += 1
                    p_ptr += 1
            elif p_ptr < len(p) - 1 and (p_ptr != len(p) - 1 and p[p_ptr + 1] == '*'):
                p_ptr += 2
                last_ptr.append([s_ptr, p_ptr])
            elif  last_ptr:
                [last_s_ptr, last_p_ptr] = last_ptr.pop()
                while last_ptr and p[last_p_ptr - 2] != s[last_s_ptr] and p[last_p_ptr - 2] != '.':
                    [last_s_ptr, last_p_ptr] = last_ptr.pop()
                
                if p[last_p_ptr - 2] == s[last_s_ptr] or p[last_p_ptr - 2] == '.':
                    last_s_ptr += 1
                    s_ptr = last_s_ptr
                    p_ptr = last_p_ptr
                    last_ptr.append([s_ptr, p_ptr])
                else:
                    return False
            else:
                return False
            
        while p_ptr < len(p) - 1 and p[p_ptr] == '.' and p[p_ptr + 1] == '*':
            p_ptr += 2
        
        return p_ptr == len(p)
    
# recursive
class Solution4:
    # @return a boolean
    def isMatch(self, s, p):
        if not p:
            return not s
        
        if len(p) == 1 or p[1] != '*':
            if len(s) > 0 and (p[0] == s[0] or p[0] == '.'):
                return self.isMatch(s[1:], p[1:])
            else:
                return False
        else:
            while len(s) > 0 and (p[0] == s[0] or p[0] == '.'):
                if self.isMatch(s, p[2:]):
                    return True
                s = s[1:]
            return self.isMatch(s, p[2:])

class Solution:
    # @return a boolean
    def isMatch(self, s, p):
        previousRow = [True]
        for i in range(0, len(p)):
            if p[i]=='*':
                previousRow.append(previousRow[i-1])
            else:
                previousRow.append(False)
                
        for letter in range(0,len(s)):
            actualRow = [False];
            for i in range(0, len(p)):
                if p[i]=='*':
                    temp = actualRow[i-1] or (previousRow[i+1] and (p[i-1]==s[letter] or p[i-1]=='.'))
                elif p[i] == '.':
                    temp = previousRow[i]
                else:
                    temp = previousRow[i] and p[i]==s[letter] 
                actualRow.append(temp)
            previousRow = actualRow
        return previousRow[len(p)]
                
if __name__ == "__main__":
    print Solution3().isMatch("abab", "a*b*")
    print Solution().isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c")
    print Solution().isMatch("aa","a")
    print Solution().isMatch("aa","aa")
    print Solution().isMatch("aaa","aa")
    print Solution().isMatch("aa", "a*")
    print Solution().isMatch("aa", ".*")
    print Solution().isMatch("ab", ".*")
    print Solution().isMatch("aab", "c*a*b")
