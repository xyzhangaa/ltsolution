###Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

def combine(n, k):
	def dfs(start, valuelist,count):
		if count == k: ret.append(valuelist); return
		for i in range(start, n + 1):
			count += 1
	                dfs(i + 1, valuelist + [i],count)
	                count -= 1
	ret = []
	dfs(1, [],0)
	return ret
