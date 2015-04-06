###Given a linked list, determine if it has a cycle in it.

###Follow up:
###Can you solve it without using extra space?

class ListNode:
	def __int__(self,x):
		self.val = x
		self.next = None

def LinkedListCycle(self,head):
  if head == None or head.next == None:
    return False
  slow = fast = head
  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
      return True
  return False
