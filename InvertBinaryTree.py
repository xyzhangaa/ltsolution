# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

####Recursive
class Solution:
    # @param {TreeNode} root
    # @return {TreeNode}
    def invertTree(self, root):
        if root==None:
            return None
        if root.left:
            self.invertTree(root.left)
        if root.right:
            self.invertTree(root.right)
        root.left, root.right = root.right,root.left
        return root

####Iterative
class Solution:
    # @param {TreeNode} root
    # @return {TreeNode}
    def invertTree(self, root):
        if root == None:
            return None
        queue = [root]
        while queue:
            front = queue.pop(0)
            if front.left:
                queue.append(front.left)
            if front.right:
                queue.append(front.right)
            front.left, front.right = front.right,front.left
        return root
