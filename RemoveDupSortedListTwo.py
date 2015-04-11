###Given a sorted linked list, delete all nodes that have duplicate numbers, 
###leaving only distinct numbers from the original list.

###For example,
###Given 1->2->3->3->4->4->5, return 1->2->5.
###Given 1->1->1->2->3, return 2->3.

class ListNode:
	def __init__(self,x):
		self.val = x
		self.next = None

def RemoveDupSortedLinkedListTwo(self,head):
	if head == None or head.next == None:
		return Head
	dummy = ListNode(0)
	dummy.next = head
	p = dummy
	temp = dummy.next
	while p.next:
		while temp.next and temp.next.val == p.next.val:
			temp = temp.next
		if temp == p.next:
			temp = p.next
			p = p.next
		else:
			p.next = temp.next
	return dummy.hext
