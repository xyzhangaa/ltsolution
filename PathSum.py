###Given a binary tree and a sum, determine if the tree has a root-to-leaf path 
###such that adding up all the values along the path equals the given sum.

#O(n), O(1)
class TreeNode:
	def __int__(self,x):
		self.val=x
		self.left = None
		self.right = None

def PathSum(root,target):
	if root == None:
		return False
	if root.left==None and root.right ==None:
		return root.val==target
	return PathSum(root.left,target-root.val) or PathSum(root.right, \
							     target-root.val)
