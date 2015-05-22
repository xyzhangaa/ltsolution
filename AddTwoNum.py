#Time: O(n)
#Space: O(1)

###You are given two linked lists representing two non-negative numbers. 
###The digits are stored in reverse order and each of their nodes contain 
###a single digit. Add the two numbers and return it as a linked list.
class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def addTwoNumbers(self, l1, l2):
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        dummy = ListNode(0)
        curr = dummy; carry = 0
        while l1 and l2:
            val = l1.val+l2.val+carry
            curr.next = ListNode(val%10)
            carry = val/10
            curr=curr.next
            l1=l1.next
            l2=l2.next
        while l1:
            val = l1.val+carry
            curr.next = ListNode(val%10)
            carry = val/10
            curr=curr.next
            l1=l1.next
        while l2:
            val = l2.val+carry
            curr.next = ListNode(val%10)
            carry = val/10
            curr=curr.next
            l2=l2.next
        if carry == 1:
            curr.next = ListNode(carry)
        return dummy.next
  
