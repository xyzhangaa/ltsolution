###Follow up for problem "Populating Next Right Pointers in Each Node".

###What if the given tree could be any binary tree? Would your previous solution still work?

###Note:

###You may only use constant extra space.

#O(n), O(1)
class TreeLinkedNode:
  def __int__(self,x):
    self.val = x
    self.left= None
    self.right = None
    self.next = None

###step by step, similar to PopulateNodes
def PopulateNodesTwo(root):
	if root:
		if root.left and root.right:
			root.left.next = root.right
			temp = root.next
			while temp:
				if temp.left:
					root.right.next = temp.left
					break
				if temp.right:
					root.right.next = temp.right
					break
				temp = temp.next
		elif root.left:
			temp = root.next
			while temp:
				if temp.left:
					root.left.next = temp.left
					break
				if temp.right:
					root.right.next = temp.right
					break
				temp = temp.next
		elif root.right:
			temp = root.next
			while temp:
				if temp.left:
					root.right.next = temp.left
					break
				if temp.right:
					root.right.next = temp.right
					break
				temp = temp.next
		PopulateNodesTwo(root.right)
		PopulateNodesTwo(root.left)


### More concise way
def PopulateNodesTwo(root):
	if root:
		p = root
		q = None
		nextNode = None
		while p:
			if p.left:
				if q:
					q.next = p.left
				q = p.left
				if nextNode == None:
					nextNode = q
			if p.right:
				if q:
					q.next = p.right
				q = p.right
				if nextNode == None:
					nextNode = q
			p = p.next
		PopulateNodesTwo(nextNode)


if __name__ == "__main__":
    root, root.left, root.right = TreeNode(1), TreeNode(2), TreeNode(3)
    root.left.left, root.left.right, root.right.right = TreeNode(4), TreeNode(5), TreeNode(7)
    Solution().connect(root)
    print root
    print root.left
    print root.left.left
