###Sort a linked list in O(n log n) time using constant space complexity.

### fast and slow pointers

class ListNode:
	def __int__(self,x):
		self.val = x
		self.next = None
		
def merge(self, head1,head2):
	if head1 == None:
		return head2
	if head2 == None:
		return head1
	dummy = ListNode(0)
	p = dummy
	while head1 and head2:
		if head1.val <= head2.val:
			p.next = head1
			head1 = head1.next
			p = p.next
		else:
			p.next = head2
			head2 = head2.next
			p = p.next
	if head1 == None:
		p.next = head2
	if head2 == None:
		p.next = head1
	return dummy
	
def sortlist(self,head):
	if head == None or head.next == None:
		return head
	slow = head
	fast = head
	while fast.next and fast.next.next:
		slow = slow.next
		fast = fast.next.next
	head1 = head
	head2 = slow.next
	slow.next = None
	head1 = self.sortlist(head1)
	head2 = self.sortlist(head2)
	head = self.merge(head1,head2)
	return head
