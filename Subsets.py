###Given a set of distinct integers, S, return all possible subsets.

###Note:
###Elements in a subset must be in non-descending order.
###The solution set must not contain duplicate subsets.
###For example,
###If S = [1,2,3], a solution is:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

def Subsets(s):
	def dfs(depth, start, valuelist):
		result.append(valuelist)
		if depth == len(s):
			return
		for i in range(start,len(s)):
			dfs(depth+1,start+1,valuelist+[s[i]])
	s.sort()
	result = []
	dfs(0,0,[])
	return result
