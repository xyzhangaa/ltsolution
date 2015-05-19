###Given a binary tree, determine if it is a valid binary search tree (BST).

###Assume a BST is defined as follows:

###The left subtree of a node contains only nodes with keys less than the node's key.
###The right subtree of a node contains only nodes with keys greater than the node's key.
###Both the left and right subtrees must also be binary search trees.

#O(n), O(1)
def ValidBST(root,min,max):
	if root == None:
		return True
	if root.val <= min or root.val >= max:
		return False
	return ValidBst(root.left,min,root.val) and ValidBST(root.right, root.val, max)

def isValidBST(root):
	return ValidBST(root,-2147483648,2147483647)
