###Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

class ListNode:
	def __int__(self,x):
		self.val = x
		self.next = None

def LinkedListCycleII(self,head):
  if head == None or head.next == None:
    return None
  slow = fast = head
  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if fast == slow:
      break
  if slow == fast:
    slow = head
    while slow != fast:
      slow = slow.next
      fast = fast.next
    return slow
  return None
