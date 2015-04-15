###Design and implement a data structure for Least Recently Used (LRU) cache. 
###It should support the following operations: get and set.

###get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
###set(key, value) - Set or insert the value if the key is not already present. 
###When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

###Hashmap
class LRUCache:
	def __int__(self,capacity):
		LRUCache.capacity = capacity
		LRUCache.length = 0
		LRUCache.dict = colleciton.OrderedDict()
	def get(self,key):
		try:
			value = LRUCache.dict[key]
			del LRUCache.dict[key]
			LRUCache.dict[key] = value
			return value
		except:
			return -1
	def set(self,key,value):
		try:
			del LRUCache.dict[key]
			LRUCache.dict[key] = value
		except:
			if LRUCache.length == LRUCache.capacity:
				LRUCache.dict.popitem(last = False)
				LRUCache.length -= 1
			LRUCache.dict[key] = value
			LRUCache.length += 1
			
###Double-linked List
class Node:
	def __int__(self,k,x):
		self.key = k
		self.val = x
		self.prev = None
		self.next = None
		
class DoubleLinkedList:
	def __int__(self):
		self.tail = None
		self.head = None
	def isEmpty():
		return not self.tail
	def removeLast(self):
		self.remove(self.tail)
	def remove(self,node):
		if self.node == self.tail:
			self.head,self.tail = None, None
			return
		if node == self.head:
			node.next.prev = None
			self.head = node.next
			return
		if node == self.tail:
			node.prev.next = None
			self.tail = node.prev
			return
		node.prev.next = node.next
		node.next.prev = node.prev
	def addFrist(self,node):
		if not self.head:
			self.head = self.tail=node
			node.prev = node.next = None
		node.next = self.head
		self.head.prev = node
		self.head = node
		node.prev = None
		
class LRUCache:
	def __int__(self,capacity):
		self.capacity = capacity
		self.size = 0
		self.P = dict()
		self.cache=DoubleLinkedList()
	def get(self,key):
		if (key in self.P) and self.P(key):
			self.cache.remove(self.P[key])
			self.cache.addFirst(self.P[key])
			return self.P[key].val
		else:
			return -1
	def set(self,key,value):
		if key in self.P:
			self.cache.remove(self.P[key])
			self.cache.addFirst(self.P[key])
			self.P[key].val = value
		else:
			node = Node(key,value)
			self.P[key] = node
			self.cache.addFirst(node)
			self.size += 1
			if self.size > self.capacity:
				self.size -= 1
				del self.P[self.cache.tail.key]
				self.cache.removeLast()
