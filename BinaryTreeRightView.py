###Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

class Solution:
  def rightsideview(self,root):
    ans = []
    if root == None:
      return []
    queue = [root]
    while queue:
      size = len(queue)
      for r in range(size):
        top = queue.pop(0)
        if r == 0:
          ans.append(top.val)
        if top.right:
          queue.append(top.right)
        if top.left:
          queue.append(top.left)
    return ans
