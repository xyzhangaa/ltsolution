###Given a binary tree, return the postorder traversal of its nodes' values.

###Iterative
def itervative_postorder(root,list):
	stack = []
	pre = None
	if root:
		stack.append(root)
		while stack:
			curr = stack[-1]
			if (curr.left == None and curr.right == None) or \
			   (pre and (pre == curr.left or pre == curr.right)):
				list.append(curr.val)
				stack.pop()
				pre = curr
			else:
				if curr.right:
					stack.append(curr.right)
				if curr.left:
					stack.append(curr.left)
					
def postorder(root):
	list = []
	interative_postorder(root,list)
	return list


###Recursive
def recursive_postorder(root,list):
	if root:
		recursive_postorder(root.left,list)
		recursive_postorder(root.right,list)
		list.append(root.val)
