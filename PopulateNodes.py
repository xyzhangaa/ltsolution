###Given a Binary Tree,
###Populate each next pointer to point to its next right node. 
###If there is no next right node, the next pointer should be set to NULL.

###Initially, all next pointers are set to NULL.

###Note:

###You may only use constant extra space.
###You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).

class TreeLinkNode:
	def __int__(self,x):
		self.val = x
		self.left = None
		self.right = None
		self.next = None

def PopulateNodes(root):
	if root and root.left:
		root.left.next = root.right
		if root.next:
			root.right.next = root.next.left
		else:
			root.right.next = None
		PopulateNodes(root.left)
		PopulateNodes(root.right)
