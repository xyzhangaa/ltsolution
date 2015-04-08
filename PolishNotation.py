###Evaluate the value of an arithmetic expression in Reverse Polish Notation.
###Valid operators are +, -, *, /. Each operand may be an integer or another expression.

###Some examples:
###["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
###["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6

def PolishNotation(s):
	stack = []
	for i in range(len(s)):
		if s[i] != '+' and s[i] != '-' and s[i] != '*' \
		   and s[i] != '/':
			stack.append(int(s[i]))
		else:
			a = stack.pop()
			b = stack.pop()
			if s[i] == '+':
				stack.append(a+b)
			elif s[i] == '-':
				stack.append(b-a)
			elif s[i] == '*':
				stack.append(a*b)
			elif s[i] == '/':
				stack.append(b/a)
	return stack.pop()
