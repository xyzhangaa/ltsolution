###Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) 
###parentheses substring.

###For "(()", the longest valid parentheses substring is "()", which has length = 2.

###Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.

def longestvalidparenthese(s):
	maxlen = 0
	stack = []
	for i in range(len(s)):
		if s[i] == '(':
			stack.append(i)
		else:
			if stack == []:
				last = i
			else:
				stack.pop()
				if stack == []:
					maxlen = max(maxlen,i-last)
				else:
					maxlen = max(maxlen,stack[len(stack)-1])
	return maxlen
