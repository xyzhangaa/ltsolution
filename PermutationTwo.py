###Given a collection of numbers that might contain duplicates, return all possible unique permutations.

###For example,
###[1,1,2] have the following unique permutations:
###[1,1,2], [1,2,1], and [2,1,1].

def PermutationTwo(num):
	if len(num) == 0:
		return []
	if len(num) == 1:
		return [num]
	num.sort()
	result = []
	previousNum = None
	for i in range(len(num)):
		if num[i] == previousNum:
			continue
		previousNum = num[i]
		for j in PermutationTwo(num[:i]+num[i+1:]):
			result.append([num[i]]+j)
	return result
