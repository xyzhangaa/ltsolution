###Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
###You should preserve the original relative order of the nodes in each of the two partitions.

class ListNode:
  def __int__(self,x):
    self.val = x
    self.next = None

def PartitionList(head,a):
  head1 = ListNode(0)
  head2 = ListNode(0)
  temp = head
  phead1 = head1
  phead2 = head2
  while temp:
    if temp.val < a:
      phead1.next = temp
      temp = temp.next
      phead1 = phead1.next
      phead1.next = None
    else:
      phead2.next = temp
      temp = temp.next
      phead2 = phead2.next
      phead2.next = None
  phead1.next=head2.next
  head=head1.next
  return head
