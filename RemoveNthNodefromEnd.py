###Given a linked list, remove the nth node from the end of list and return its head.
# Time:  O(n)
# Space: O(1)
#
# Given a linked list, remove the nth node from the end of list and return its head.
# 
# For example,
# 
#    Given linked list: 1->2->3->4->5, and n = 2.
# 
#    After removing the second node from the end, the linked list becomes 1->2->3->5.
# Note:
# Given n will always be valid.
# Try to do this in one pass.

class Solution:
def remnthnodefromend(head,n):
  current = head
  previous = head
  for _ in range(n-1):
    previous.next = head.next
  if previous.next == None:
    head = head.next
  else:
    previous.next=previous.next
    while previous.next!=None:
      previous.next = previous.next
      current.next = current.next
    current.next = current.next.next
  return head
  
if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    
    print Solution().removeNthFromEnd(head, 2)
