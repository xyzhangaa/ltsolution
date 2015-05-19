###Reverse a linked list from position m to n. Do it in-place and in one-pass.

###For example:
###Given 1->2->3->4->5->NULL, m = 2 and n = 4,

###return 1->4->3->2->5->NULL.

###Note:
###Given m, n satisfy the following condition:
###1 ≤ m ≤ n ≤ length of list.

#O(n), O(1)
class ListNode:
	def __init__(self,x):
		self.val = x
		self.next = None

def ReverseLinkedListTwo(self,head,m,n):
	if m==n or head == None or head.next == None:
		return head
	dummy = ListNode(0)
	dummy.next = head
	head1=dummy
	for i in range(m-1):
		head1=head1.next
	p = head1.next
	for i in range(n-m):
		temp = head1.next
		head1.next = p.next
		p.next = p.next.next
		head1.next.next = temp
	return dummy.next
