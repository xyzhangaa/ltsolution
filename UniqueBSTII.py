###Given n, generate all structurally unique BST's (binary search trees) that store values 1...n.
###List the Tree Nodes


#O(4^n/n^(3/2)), O(4^n/n^(3/2))
class TreeNode:
	def __int__(self,x):
		self.val=x
		self.left = None
		self.right = None
		
def dfs(self, start,end):
	if start > end:
		return [None]
	res = []
	for rootval in range(start,end+1):
		lefttree = self.dfs(start,rootval-1)
		righttree = self.dfs(rootval+1,end)
		for i in lefttree:
			for j in righttree:
				root = TreeNode(rootval)
				root.left = i
				root.right = j
				res.append(root)
	return res
	
def generateBTS(n):
	return self.dfs(1,n)
