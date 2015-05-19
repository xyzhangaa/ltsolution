###Two elements of a binary search tree (BST) are swapped by mistake.

###Recover the tree without changing its structure.

#O(n), O(1)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {void} Do not return anything, modify root in-place instead.
            
    def recoverTree(self, root):
        return self.morristraversal(root)
    
    def morristraversal(self,root):
        if root is None:
            return 
        broken = [None,None]
        pre, cur = None,root
        while cur:
            if cur.left is None:
                self.detectbroken(broken,pre,cur)
                pre =cur
                cur = cur.right
            else:
                node= cur.left
                while node.right and node.right != cur:
                    node = node.right
                if node.right is None:
                    node.right = cur
                    cur = cur.left
                else:
                    self.detectbroken(broken,pre,cur)
                    node.right  = None
                    pre = cur
                    cur = cur.right
        broken[0].val,broken[1].val = broken[1].val,broken[0].val

    def detectbroken(self,broken,pre,cur):
        if pre and pre.val > cur.val:
            if broken[0] is None:
                broken[0] = pre
            broken[1] =cur
