###Given a collection of integers that might contain duplicates, S, return all possible subsets.

###Note:

###Elements in a subset must be in non-descending order.
###The solution set must not contain duplicate subsets.

#O(n*2^n), O(1)

##Recursively
def SubsetsTwo(s):
	def dfs(depth, start, valuelist,res):
		if valuelist not in result:
			result.append(valuelist)
		if depth == len(s):
			return
		for i in range(start,len(s)):
			dfs(depth+1,i+1,valuelist+[s[i]],res)
	s.sort()
	res = []
	dfs(0,0,[],res)
	return res

###Iteratively
class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        result = []
        i, count = 0, 1 << len(S)
        S = sorted(S)
        
        while i < count:
            cur = []
            for j in xrange(len(S)):
                if i & 1 << j:
                    cur.append(S[j])
            if cur not in result:
                result.append(cur)
            i += 1
            
        return result
