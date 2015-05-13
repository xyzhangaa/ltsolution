###Given preorder and inorder traversal of a tree, construct the binary tree.

###Note: You may assume that duplicates do not exist in the tree.

def ConstructBTPreInorder(preorder,inorder):
	if len(preorder) == 0:
		return None
	if len(preorder) == 1:
		return TreeNode(preorder[0])
	root = TreeNode(preorde[0])
	index = inorder.index(preorder[0])
	root.left = ConstructBTPreInorder(preorder[1:index+1],inorder[0:index])
	root.right = ConstructBTPreInorder(preorder[index+1:len(preorder)], \
					   inorder[index+1:len(inorder)])
	return root
