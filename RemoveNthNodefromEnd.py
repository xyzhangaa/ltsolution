###Given a linked list, remove the nth node from the end of list and return its head.
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
