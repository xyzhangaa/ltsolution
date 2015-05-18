###Given a digit string, return all possible letter combinations that the number could represent.

# Time:  O(n * 4^n)
# Space: O(n)
# Recursive Solution
def LCPN(numstr):
		num2str = {'0':' ', '1':' ', '2': 'abc', '3': 'def', '4':'ghi', \
		   '5': 'lmn', '6': 'opq', '7':'rst','8':'uvw', \
		   '9':'xyz'}
		if len(numstr) == 0:
			return ' '
		if len(numstr) == 1:
			return [i for i in num2str[numstr[0]]]
		temp = [i for i in num2str[numstr[0]]]
		result = []
		for i in LCPN(numstr[1:]):
			result.extend([j+i for j in temp])
		return result

# Iterative Solution
# Time:  O(n * 4^n)
# Space: O(n)
class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        lookup, result = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"], [""]

        for digit in digits:
            choices = lookup[int(digit)]
            m, n = len(choices), len(result)
            result.extend([result[i % n] for i in xrange(n, m * n)])    

            for i in xrange(m * n):
                result[i] += choices[i / n]
            
        return result
