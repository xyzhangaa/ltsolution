Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

You may assume that the given expression is always valid.


class Solution:
    # @param {string} s
    # @return {integer}
    def calculate(self, s):
        s = re.sub(r'\d+', ' \g<0> ', s)
        op = {'+': operator.add, '-': operator.sub,
              '*': operator.mul, '/': operator.floordiv}
        expression = s.split()
        total = d = idx = 0
        func = op['+']
        while idx < len(expression):
            e = expression[idx]
            if e in '+-':
                total = func(total, d)
                func = op[e]
            elif e in '*/':
                idx += 1
                d = op[e](d, int(expression[idx]))
            else:
                d = int(e)
            idx += 1
        return func(total, d)
