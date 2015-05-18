###Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

###If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

###You may not alter the values in the nodes, only nodes itself may be changed.

###Only constant memory is allowed.

###For example, Given this linked list: 1->2->3->4->5

###For k = 2, you should return: 2->1->4->3->5

###For k = 3, you should return: 3->2->1->4->5

###class ListNode:
###	def __init__(self,x):
###		self.val = x
###		self.next = None

#time O(n)
#space O(1)
class Solution:
	def reverse(self,start,end):
		newhead = ListNode(0)
		newhead.next = start
		while newhead.next!= end:
			temp  = start.next
			start.next = temp.next
			temp.next = newhead.next
			newhead.next = temp
		return [end,start]

	def reverseKgroup(head,k):
		if head == None:
			return None
		nhead = ListNode(0)
		nhead.next = head
		start = nhead
		while start.next:
			end = start
			for i in range(k-1):
				end = end.next
				if end.next == None:
					return nhead.next
			result = self.reverse(start.next,end.next)
			start.next = result[0]
			start = result[1]
		return nhead.next

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    print Solution().reverseKGroup(head, 2)
