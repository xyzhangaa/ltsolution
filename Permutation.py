###Given a collection of numbers, return all possible permutations.

###For example,
###[1,2,3] have the following permutations:
###[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].

def Permutation(num):
	if len(num) == 0:
		return []
	if len(num) == 1:
		return [num]
	result = []
	for i in range(len(num)):
		for j in Permutation(num[:i]+num[i+1:]):
			result.append([num[i]]+j)
	return result
