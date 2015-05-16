### Itervatively

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        if head == None or head.next == None:
            return head
        prev = None
        curr = head
        while curr:
            next = curr.next
            curr.next=prev
            prev = curr
            curr = next
        head = prev
        return prev
        
### Recursively

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        if head == None or head.next == None:
            return head
        newhead = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return newhead

