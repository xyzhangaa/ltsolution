###Given a binary tree, determine if it is height-balanced.

###For this problem, a height-balanced binary tree is defined as a binary tree in 
###which the depth of the two subtrees of every node never differ by more than 1.

#O(n), O(1)
def height(root):
	if root ==None:
		return 0
	return max(height(root.left),height(root.right))+1
	
def BalancedBT(root):
	if root == None:
		return True
	if abs(height(root.left)-height(root.right)) <= 1:
		return BalancedBT(root.left) and BalancedBT(root.right)
	else:
		return False
