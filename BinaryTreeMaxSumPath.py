###Given a binary tree, find the maximum path sum.

###The path may start and end at any node in the tree.

class Solution:
	def maxsum(root):
		if root == None:
			return 0
		sum = root.val
		lmax = 0
		rmax = 0
		if root.left:
			lmax = maxsum(root.left)
			if lmax > 0:
				sum += lmax
		if root.right:
			rmax = maxsum(root.right)
			if rmax > 0:
				sum+= rmax
		if sum > Solution.max:
			Solution.max = sum
		return max(root.val,max(root.val+lmax,root.val+right))

	def maxPathSum(root):
		Solution.max = -10000000
		if root == None:
			return 0
		maxsum(root)
		return Solution.max
