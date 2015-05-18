###Given an array of strings, return all groups of strings that are anagrams.
###Note: All inputs will be in lower-case.
#time O(n*k*logk)
#time O(n)

def anagram(strs):
	htable = {}
	for item in strs:
		sortedword = ''.join(sorted(item))
		if sortedword not in htable:
			htable[sortedword] = [item]
		else:
			htable[sortedword] += [item]
	result = []
	for item in htable:
		if len(htable[item]) >= 2:
			result.append(htable[item])
	return result
