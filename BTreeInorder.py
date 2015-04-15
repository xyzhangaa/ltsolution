###Given a binary tree, return the inorder traversal of its nodes' values.

def iterative_inorder(root,list):
	stack = []
	while root or stack:
		if root:
			stack.append(root)
			root = root.left
		else:
			root = stack.pop()
			list.append(root.val)
			root= root.right
	return list
	
def inorder(root):
	list = []
	iterative_inorder(root,list)
	return list
