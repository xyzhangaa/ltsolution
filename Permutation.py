###Given a collection of numbers, return all possible permutations.

###For example,
###[1,2,3] have the following permutations:
###[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].
## Time:  O(n!)
# Space: O(n)

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

class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        result = []
        used = [False] * len(num)
        self.permuteRecu(result, used, [], num)
        return result
    
    def permuteRecu(self, result, used, cur, num):
        if len(cur) == len(num):
            result.append(cur + [])
            return
        for i in xrange(len(num)):
            if not used[i]:
                used[i] = True
                cur.append(num[i])
                self.permuteRecu(result, used, cur, num)
                cur.pop()
                used[i] = False
