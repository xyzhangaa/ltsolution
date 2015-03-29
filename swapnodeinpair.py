###Given a linked list, swap every two adjacent nodes and return its head.
    
    def swapPairs(head):
        if head == None or head.next == None:
            return head
        dummy = ListNode(0)
        dummy.next = head
        p = dummy
        while p.next and p.next.next:
            tmp = p.next.next
            p.next.next = tmp.next
            tmp.next = p.next
            p.next = tmp
            p = p.next.next
        return dummy.next
