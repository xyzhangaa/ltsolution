###Given a binary tree, flatten it to a linked list in-place.

#O(n), O(1)
def FlatBT(root):
	if root == None:
		return
	FlatBT(root.left)
	FlatBT(root.right)
	p = root
	if p.left == None:
		return
	p = p.left
	while p.right:
		p = p.right
	p.right = root.right
	root.right = root.left
	root.left = None
