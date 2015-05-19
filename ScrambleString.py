###https://oj.leetcode.com/problems/scramble-string/

# O(n^4), O(n)
class Solution:
    # @param {string} s1
    # @param {string} s2
    # @return {boolean}
    def isScramble(self, s1,s2):
        n, m = len(s1), len(s2)
        if n != m or sorted(s1) != sorted(s2):
            return False
        if n <4 or s1 == s2:
            return True
        for i in range(1,n):
            if (self.isScramble(s1[:i],s2[:]) and self.isScramble(s1[i:],s2[i:])) or (self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i])):
                return True
        return False

##3-D DP Solution
# O(n^3), O(n^3) 
class Solution:
    # @param {string} s1
    # @param {string} s2
    # @return {boolean}
    def isScramble(self, s1, s2):
        if len(s1) != len(s2):
            return False
        if len(s1) == 0:
            return True
        self.s1, self.s2 = s1, s2
        lens = len(s1)
        self.dp = [[[-1] * lens for i in range(lens)] * lens for i in range(lens)]
        return self.dfs(0, 0, len(s1))
    
    def dfs(self, lp, rp, len):
        if self.dp[lp][rp][len - 1] >= 0:
            return True if self.dp[lp][rp][len - 1] == 1 else False
        if len == 1:
            return self.s1[lp] == self.s2[rp]
        for i in range(1, len):
            if self.dfs(lp, rp, i) and self.dfs(lp + i, rp + i, len - i) \
                    or self.dfs(lp, rp + i, len - i) and self.dfs(lp + len - i, rp, i):
                self.dp[lp][rp][len - 1] = 1
                return True
        self.dp[lp][rp][len - 1] = 0 
        return False
