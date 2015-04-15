###Given a binary tree, find its minimum depth.

###The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

def MinDepthBTree(root):
	if root == None:
		return 0
	if root.left == None and root.right != None:
		return MinDepthBTree(root.right)+1
	if root.left != None and root.right == None:
		return MinDepthBTree(root.left)+1
	return min(MinDepthBTree(root.left),MinDepthBTree(root.right))+1
