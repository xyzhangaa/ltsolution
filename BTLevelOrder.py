###Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

#O(n), O(n)
def preorder(root,level,res):
	if root:
		if len(res) < level +1:
			res.append([])
		res[level].append(root.val)
		preorder(root.left,level+1,res)
		preorder(root.right,level+1,res)
		
def BTLevelOrder(root):
	res = []
	preorder(root,0,res)
	return res
