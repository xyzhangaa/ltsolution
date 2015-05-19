###Validate if a given string is numeric.
#time O(n)
#space O(1)
def ValidNum(s):
	INVALID = 0
	SPACE = 1
	SIGN = 2
	DIGIT = 3
	DOT = 4
	EXPONENT = 5
	transitionTable = [[-1,0,3,1,2,-1],[-1,8,-1,1,4,5],[-1,-1,-1,4,-1,-1], \
			   [-1,-1,-1,1,2,-1],[-1,8,-1,4,-1,5],[-1,-1,6,7,-1,-1],
			   [-1,-1,-1,7,-1,-1],[-1,8,-1,7,-1,-1],[-1,8,-1,-1,-1,
								 -1]]
	state = 0
	i = 0
	while i < len(s):
		inputtype = INVALID
		if s[i] == ' ':
			inputtype = SPACE
		elif s[i] == '-' or s[i] == '+':
			inputtype = SIGN
		elif s[i] in '0123456789':
			inputtype = DIGIT
		elif s[i] == '.':
			inputtype = DOT
		elif s[i] == 'e' or s[i] == 'E':
			inputtype = EXPONENT
		state = transitionTable[state][inputtype]
		if state == -1:
			return False
		else:
			i+= 1
	return state == 1 or state == 4 or state == 7 or state == 8

class Solution2:
    # @param s, a string
    # @return a boolean
    def isNumber(self, s):
        import re
        return bool(re.match("^\s*[\+\-]?((\d+(\.\d*)?)|\.\d+)([eE][+-]?\d+)?\s*$", s))
