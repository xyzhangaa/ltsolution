###Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

def ConvertArrayBST(A):
	length = len(A)
	if length == 0:
		return None
	if length == 1:
		return TreeNode(A[0])
	root = TreeNode(A[length/2])
	root.left = ConvertArrayBST(A[:length/2])
	root.right = ConvertArrayBST(A[length/2+1:])
	return root
	
def ConvertListBST(head):
	array = []
	p = head
	while p:
		array.append(p.val)
		p = p.next
	return ConvertArrayBST(array)
