###Given a list, rotate the list to the right by k places, where k is non-negative.

###For example:
###Given 1->2->3->4->5->NULL and k = 2,
###return 4->5->1->2->3->NULL.
#time O(n)
#space O(1)
def rotatelist(self,head,k):
	if k ==0 :
		return head
	if head == None:
		return None
	dummy = ListNode(0)
	dummy.next = head
	p = dummy
	count = 0
	while p.next:
		p = p.next
		count += 1
	p.next = dummy.next
	move = count-(k%count)
	for i in range(move):
		p=p.next
	head = p.next
	p.next = None
	return head
