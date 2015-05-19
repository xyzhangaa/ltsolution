###Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

class ListNode:
	def __int__(self,x):
		self.val = x
		self.next = None

def LinkedListCycleII(self,head):
  if head == None:
    return None
  hascycle = None
  slow = fast = head
  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if fast == slow:
      hascycle= True
      break
  if not hascycle:
  	return None
  if slow == fast:
    fast = head
    while slow != fast:
      slow = slow.next
      fast = fast.next
    return slow
