###Merge two sorted linked lists and return it as a new list. The new list should be 
###made by splicing together the nodes of the first two lists.

class ListNode(self,x):
	self.val = x
	self.next = None

def mergetwosortedlinkedlist(self,l1,l2):
	if l1 == None:
		return l2
	if l2 == None:
		return l2
	dummy = ListNode(0)
	temp = dummy
	while l1 and l2:
		if l1.val <= l2.val:
			temp.next = l1
			l1 = l1.next
			temp = temp.next
		else:
			temp.next = l2
			l2 = l2.next
			temp = temp.next
	if l1 == None:
		temp.next = l2
	else:
		temp.next =l1
	return dummy.next
