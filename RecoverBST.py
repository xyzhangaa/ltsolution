###Two elements of a binary search tree (BST) are swapped by mistake.

###Recover the tree without changing its structure.

def FindTwoNodes(root):
	if root:
		FindTwoNodes(root.left)
		if prev and prev.val > root.val:
			n2 = root
			if n1 == None:
				n1 = prev
		prev = root
		FindTwoNodes(root.right)
		
def RecoverBST(root):
	n1 = n2 = None
	prev = None
	FindTwoNodes(root)
	n1.val,n2.val = n2.val,n1.val
	return root
