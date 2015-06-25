Given a complete binary tree, count the number of nodes.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def countNodes(self, root):
        if root == None:
            return 0
        leftheight,rightheight=0,0
        pleft = TreeNode(0)
        pleft = root
        while pleft:
            leftheight += 1
            pleft = pleft.left
        pright = TreeNode(0)
        pright = root
        while pright:
            rightheight += 1
            pright = pright.right
        if leftheight == rightheight:
            return 2**leftheight-1
        return self.countNodes(root.left)+self.countNodes(root.right)+1
