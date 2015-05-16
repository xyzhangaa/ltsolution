###Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

class Solution:
    # @param {integer} n
    # @return {string[]}
    def helper(self, l, r, item, res):
        if r < l:
            return
        if l == 0 and r ==0:
            res.append(item)
        if l > 0:
            self.helper(l-1,r,item+'(',res)
        if r > 0:
            self.helper(l,r-1,item+')',res)
    def generateParenthesis(self, n):
        if n == 0:
            return []
        res = []
        self.helper(n,n,'',res)
        return res
