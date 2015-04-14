###Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

class TreeNode:
	def __int__(self,x):
		self.val = x
		self.left = None
		self.right = None
		
def help(p,q):
	if p == None and q == None:
		return True
	if p and q and p.val == q.val:
		return help(p.right,q.left) and help(p.left,q.right)
	return False

def SymmetricTree(root):
	if root:
		return help(root.left,root.right)
	return True
