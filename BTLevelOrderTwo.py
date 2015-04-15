###Given a binary tree, return the bottom-up level order traversal of its nodes' values. 
333(ie, from left to right, level by level from leaf to root).

def preorder(root,level,res):
	if root:
		if len(res) < level +1:
			res.append([])
		res[level].append(root.val)
		preorder(root.left,level+1,res)
		preorder(root.right,level+1,res)
		
def BTLevelOrderTwo(root):
	res = []
	preorder(root,0,res)
	res.reverse()
	return res
