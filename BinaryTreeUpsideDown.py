# Time:  O(n)
# Space: O(1)
#
# Given a binary tree where all the right nodes are either leaf nodes with a sibling 
# (a left node that shares the same parent node) or empty, flip it upside down and 
# turn it into a tree where the original right nodes turned into left leaf nodes. 
# Return the new root.
# 
# For example:
# Given a binary tree {1,2,3,4,5},
# 
#     1
#    / \
#   2   3
#  / \
# 4   5
# 
# return the root of the binary tree [4,5,2,#,#,3,1].
# 
#    4
#   / \
#  5   2
#     / \
#    3   1  
#

class Solution:
  def upsidedownbinarytree(self,root):
    p,parent,parent_right = root,None,None
    while p:
      left = p.left
      p.left = parent_right
      parent_right = p.right
      p.right = parent
      parent = p
      p = left
      return parent

class Solution2:
  def upsidedownbinarytree(self,root):
    return self.upsidedownbinarytreerecu(root,None)
  def upsideodwnbinarytreerecu(self,p,parent):
    if p is None:
      return parent
    root = self.upsidedownbinarytreerecu(p.left,p)
    if parent:
      p.left = parent.right
    else:
      p.left= None
    p.right = parent
    return root
