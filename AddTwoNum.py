###You are given two linked lists representing two non-negative numbers. 
###The digits are stored in reverse order and each of their nodes contain 
###a single digit. Add the two numbers and return it as a linked list.
class ListNode:
  def __int__(self,x):
    self.val = x
    self.next=None
  
def addtwonum(a,b):
  return _addtwonum(a,b,0)

def _addtwonum(a,b,carry):
  value = carry
  if b == None:
    a,b = b,a
  if a == None and b == None:
    if value = 0:
      return None
    else:
      return ListNode(value)
    elif a == None:
      value += b.val
      tempNode = ListNode(value%10)
      tempNode.next = _addtwonum(None,b.next,value/10)
      return tempNode
    else:
      value += a.val+b.val
      tempNode = ListNode(value%10)
      tempNode.next = _addtwonum(a.next,b.next,value/10)
      return tempNode
