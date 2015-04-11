###Given a binary tree, find its maximum depth.

###The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

class TreeNode:
	def __int__(self,x):
		self.val = x
		self.left = None
		self.right = None

def MaxDepthBinaryTree(self,root):
	if root == None:
		return None
	else:
		return max(MaxDepthBinaryTree(self,root.left), MaxDepthBinaryTree(self,root,right)) +1
