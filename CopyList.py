###A linked list is given such that each node contains an additional random pointer 
###which could point to any node in the list or null.

###Return a deep copy of the list.

#O(n), O(1)
def CopyList(head):
	if head == None:
		return None
	temp = head
	while temp:
		newNode = RandomListNode(temp.label)
		newNode.next= temp.next
		temp.next = newNode
		temp = temp.next.next
	temp = head
	while temp:
		if temp.random:
			temp.next.random = temp.random.next
		temp = temp.next.next
	newhead = head.next
	pold = head
	pnew = newhead
	while pnew.next:
		pold.next = pnew.next
		pold = pold.next
		pnew.next = pold.next
		pnew = pnew.next
	pold.next= None
	pnew.next= None
	return newhead
