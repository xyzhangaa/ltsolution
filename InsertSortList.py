###Sort a linked list using insertion sort.

class ListNode:
	def __int__(self,x):
		self.val = x
		self.next = None

def InsertSortList(self,head):
  if not head:
    return head
  dummy = ListNode(0)
  dummy.next = head
  curr = head
  while curr.next:
    if curr.next.val < curr.val:
      pre = dummy
      while pre.next.val < curr.next.val:
        pre = pre.next
      temp = curr.next
      curr.next = temp.next
      temp.next = pre.next
      pre.next = temp
    else:
      curr = curr.next
  return dummy.next
