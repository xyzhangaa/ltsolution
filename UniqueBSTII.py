###Given n, generate all structurally unique BST's (binary search trees) that store values 1...n.
###List the Tree Nodes

class TreeNode:
	def __int__(self,x):
		self.val=x
		self.left = None
		self.right = None
		
def dfs(start,end):
	if start > end:
		return [None]
	res = []
	for rootval in range(start,end+1):
		lefttree = dfs(start,rootval-1)
		righttree = dfs(rootval+1,end)
		for i in lefttree:
			for j in righttree:
				root = TreeNode(rootval)
				root.left = i
				root.right = j
				res.append(root)
		return res
	
def generateBTS(n):
	return dfs(1,n)
