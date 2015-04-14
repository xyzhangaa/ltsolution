###Given two binary trees, write a function to check if they are equal or not.

###Two binary trees are considered equal if they are structurally identical and the nodes have the same value.

class TreeNode:
	def __int__(self,x):
		self.val = x
		self.left = None
		self.right = None
		
def SameTree(p,q):
	if p == None and q == None:
		return True
	if p and q and p.val == q.val:
		return SameTree(p.left,q.left) and SameTree(p.right,q.right)
	return False
