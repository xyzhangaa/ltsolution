###Given a collection of integers that might contain duplicates, S, return all possible subsets.

###Note:

###Elements in a subset must be in non-descending order.
###The solution set must not contain duplicate subsets.

def SubsetsTwo(s):
	def dfs(depth, start, valuelist):
		if valuelist not in result:
			result.append(valuelist)
		if depth == len(s):
			return
		for i in range(start,len(s)):
			dfs(depth+1,i+1,valuelist+[s[i]])
	s.sort()
	result = []
	dfs(0,0,[])
	return result
