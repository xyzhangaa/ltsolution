###Given a digit string, return all possible letter combinations that the number could represent.

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
