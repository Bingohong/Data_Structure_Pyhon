# 定义双端队列结构 double-ended-queue
# 列表右侧为队首
class Deque:
	"""docstring for Deque"""
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def addFront(self, item):
		self.items.append(item)

	def addRear(self, item):
		self.items.insert(0, item)

	def removeFront(self):
		return self.items.pop()

	def removeRear(self):
		return self.items.pop(0)

	def size(self):
		return len(self.items)

#-----------------双端队列实例---------------------
# 回文词判断
def palChecker(aString):
	charDeque = Deque()
	for ch in aString:
		charDeque.addRear(ch)

	stillEqual = True

	while charDeque.size() > 1 and stillEqual:
		first = charDeque.removeFront()
		last = charDeque.removeRear()
		if first != last:
			stillEqual = False

	return stillEqual

