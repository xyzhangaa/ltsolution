###Given a binary tree, return the preorder traversal of its nodes' values.

def iterative_preorder(root,list):
	stack = []
	while root or stack:
		if root:
			list.append(root.val)
			stack.append(root)
			root = root.left
		else:
			root = stack.pop()
			root = root.right
	return list
	
def preorder(root):
	list = []
	iterative_preorder(root,list)
	return list
