###Given inorder and postorder traversal of a tree, construct the binary tree.

###Note:You may assume that duplicates do not exist in the tree.
def ConstructBTInPostoder(inorder,postorder):
	if len(inorder) ==0:
		return None
	if len(inorder) == 1:
		return TreeNode(inorder[0])
	root = TreeNode(postorder[-1])
	index = inorder.index(postorder[-1])
	root.left= ConstructBTInPostorder(inorder[:index],postorder[:index])
	root.right=ConstructBTInPostorder(inorder[:ndex+1:len(inorder)],postorder[index+1:len(postorder)-1])
	return root
