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
        curB = headA
      else:
        break
    return None

# Hash Table Solution
class SolutionII:
  def intersection(self,headA,headB):
        htable = {}
        while headA:
            htable[headA] = True
            headA = headA.next
        while headB:
            if headB in htable:
                return headB
            headB = headB.next
        return None
