# 定义队列结构
class Queue:
	"""docstring for Queue"""
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def enqueue(self, item):
		self.items.insert(0, item)

	def dequeue(self):
		return self.items.pop()

	def size(self):
		return len(self.items)

#-------------------------队列结构实例-----------------------------
#热土豆模拟
def hotPotato(namelist, num):
	simQueue = Queue()
	for name in namelist:
		simQueue.enqueue(name)

	while simQueue.size() > 1:
		for i in range(num):
			simQueue.enqueue(simQueue.dequeue())

		simQueue.dequeue()

	return simQueue.dequeue()

# 模拟打印任务
class printer:
	"""docstring for printer"""
	def __init__(self, ppm):
		self.pagerate = ppm
		self.currentTask = None
		self.timeRemaining = 0

	def tick(self):
		if self.currentTask != None:
			self.timeRemaining -= 1
			if self.timeRemaining <= 0:
				self.currentTask = None

	def busy(self):
		if self.currentTask != None:
			return True
		else:
			return False

	def startNext(self, newtask):
		self.currentTask = newtask
		self.timeRemaining = newtask.getPage() * 60 / self.pagerate

import random

class task:
	"""docstring for task"""
	def __init__(self,time):
		self.timestamp = time
		self.pages = random.randrange(1,21)#每次打印页数范围

	def getStamp(self):
		return self.timestamp

	def getPage(self):
		return self.pages

	def waitTime(self, currentTime):
		return currentTime - self.timestamp

def simulation(numSeconds, pagePerMinute):
	labprinter = printer(pagePerMinute)
	printQueue = Queue()
	waitTime = []

	for currentSecond in range(numSeconds):
		if newPrintTask():
			task = task(currentSecond)
			printQueue.enqueue(task)

		if (not labprinter.busy()) and (not printQueue.isEmpty()):
			nextTask = printQueue.dequeue()
			waitTime.append(nextTask.waitTime(currentSecond))
			labprinter.startNext(nextTask)

		labprinter.tick()

	averageWait = sum(waitTime) / len(waitTime)
	print("Average Wait %6.2f secs %3d tasks remaining." %(averageWait, printQueue.size()))

def newPrintTask():
	num = random.randrange(1,181)#平均180s出现一个打印任务
	if num == 180:
		return True
	else:
		return False


