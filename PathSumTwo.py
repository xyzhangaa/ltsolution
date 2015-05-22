###Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

#O(n), O(1)
class TreeNode:
	def __int__(self,x):
		self.val=x
		self.left = None
		self.right = None

def PathSumTwo(root,target):
	def dfs(root,curr,valuelist):
		if root.left == None and root.right == None:
			if curr == target:
				res.append(valuelist)
		if root.left:
			dfs(root.left,curr+root.left.val,valuelist+ \
			    [root.left.val])
		if root.right:
			dfs(root.right,curr+root.right.val,valuelist + \
			    [root.right.val])
	res = []
	if root == None:
		return []
	dfs(root,root.val,[root.val])
	return res
