# 定义无序链表结构
# 定义节点 Node
class Node:
	"""docstring for Node"""
	def __init__(self, initdata):
		self.data = initdata
		self.next = None

	def getData(self):
		return self.data 

	def getNext(self):
		return self.next

	def setData(self,newdata):
		self.data = newdata

	def setNext(self, newnext):
		self.next = newnext

class UnorderedList:
	"""docstring for UnorderedList"""
	def __init__(self):
		self.head = None

	def isEmpty(self):
		return self.head == None

	def add(self, item):
		temp = Node(item)
		temp.setNext(self.head)
		self.head = temp

	def size(self):
		current = self.head
		count = 0
		while current != None:
			count += 1
			current = current.getNext()
		return count

	def search(self,item):
		current = self.head
		found = False
		while current != None and not found:
			if current.getData() == item:
				found = True
			else:
				current = current.getNext()
		return found

	def remove(self, item):
		current = self.head
		previous = None
		found = False
		while current != None and not found:
			if current.getData() == item:
				found = True
			else:
				previous = current
				current = current.getNext()

		if found:
			if previous == None:
				self.head = current.getNext()
			else:
				previous.setNext(current.getNext())
		else:
			return found

	def append(self,item):
		temp = Node(item)
		previous = None
		current = self.head
		while current != None:
			previous = current
			current = current.getNext()
		if previous == None:
			self.head = temp
		else:
			previous.setNext(temp)








		

		