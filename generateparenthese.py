###Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

def _generateParenthesis(n, m):
        if n == 0:      return [")"*m]
        elif n == m:    return ["("+i for i in _generateParenthesis(n-1, m)]
        else:           return ["("+i for i in _generateParenthesis(n-1, m)] + \
                               [")"+i for i in _generateParenthesis(n, m-1)]
                               
def generateParenthesis(n):
	    return _generateParenthesis(n, n)
