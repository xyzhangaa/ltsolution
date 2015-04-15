###Given a binary tree, return the zigzag level order traversal of its nodes' values. 
###(ie, from left to right, then right to left for the next level and alternate between).

def preorder(root,level,res):
	if root:
		if len(res) < level+1:
			res.append([])
		if level %2 == 0:
			res[level].append(root.val)
		else:
			res[level].insert(0,root.val)
		preorder(root.left,level+1,res)
		preorder(root.right,level+1,res)
		
def BTZigzag(root):
	res = []
	preorder(root,0,res)
	return res
