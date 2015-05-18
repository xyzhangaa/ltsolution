# Time:  O(m + n)
# Space: O(1)

###Write a program to find the node at which the intersection of two singly linked lists begins.

class ListNode:
  def __init__(self,x):
    self.val = x
    self.next= None

class Solution:
  def intersection(self,headA,headB):
    curA, curB = headA,headB
    tailA, tailB = None, None
    while curA and curB:
      if curA == curB:
        return curA
      if curA.next:
        curA = curA.next
      elif tailA is None:
        tailA = curA
        curA = headB
      else:
        break
      if curB.next:
        curB = curB.next
      elif tailB is None:
        tailB = curB
        curB = tailA
      else:
        break
    return None
