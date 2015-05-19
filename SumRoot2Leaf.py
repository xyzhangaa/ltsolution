###Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

###An example is the root-to-leaf path 1->2->3 which represents the number 123.

###Find the total sum of all root-to-leaf numbers.

#O(n),O(h)
def sum(root,preSum):
	if root == None:
		return 0
	preSum = preSum*10+root.val
	if root.left == None and root.right == None:
		return preSum
	return sum(root.left,preSum)+sum(root.right,preSum)
	
def SumRoot2Leadf(root):
	return sum(root,0)
