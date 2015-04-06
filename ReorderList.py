###Given a singly linked list L: L0→L1→…→Ln-1→Ln, reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

###You must do this in-place without altering the nodes' values.

###For example, Given {1,2,3,4}, reorder it to {1,4,2,3}.

class ListNode:
	def __int__(self,x):
		self.val = x
		self.next = None

def ReorderList(self,head):
	if head == None or head.next == None or head.next.next == None:
		return head
	slow = fast = head
	while fast and fast.next:
		slow = slow.next
		fast = fast.next.next
	head1 = head
	head2 = slow.next
	slow.next = None
	dummy = ListNode(0)
	dummy.next = head2
	p = head2.next
	head2.next = None
	temp = p
	p = p.next
	temp.next = dummy.next
	dummy.next = temp
	head2 = dummy.next
	p1 = head1
	p2 = head2
	while p2:
		temp1 = p1.next
		temp2 = p2.next
		p1.next = p2
		p2.next = temp1
		p1 = temp1
		p2 = temp2
	return head
