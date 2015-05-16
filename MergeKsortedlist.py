###Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

class Soluiton:
  def mergeKLists(self,lists):
    heap = []
    for nodes in lists:
      if nodes:
        heap.append((node.val,nodes)):
    heapq.heapify(heap)
    head = ListNode(0); curr = head
    while heap:
      pop = heapq.heappop(heap)
      curr.next = ListNode(pop[0])
      curr = curr.next
      if pop[1].next:
        heapq.heappush(heap,(pop[1].next.val,pop[1].next))
    return head.next
      
