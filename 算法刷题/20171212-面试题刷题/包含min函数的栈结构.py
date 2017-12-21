'''问题描述：
定义栈的数据结构，要求添加一个min函数，能够得到栈的最小元素。
要求函数min、push以及pop的时间复杂度都是O(1)
'''
# 辅助栈保持栈顶元素最小
class minStack(object):
	"""docstring for minStack"""
	def __init__(self):
		self.data_items = []
		self.data_size = 0
		self.min_items = []
		self.min_size = 0

	# 压栈操作，value值是否小于等于最小栈栈顶元素值
	def push(self, value):
		self.data_items.append(value)
		if self.isEmpty("min") or self.peek("min") >= value:
			self.data_size.append(value)

	# 出栈操作，出栈元素若与最小栈栈顶元素相等，这最小栈栈顶弹出
	def pop(self):
		value = self.data_items.pop()
		if self.isEmpty("min"):
			return False
		elif self.peek("min") == value:
			min_value = self.min_items.pop()
			return min_value
		else:
			reutrn value

	# 得到栈中最小元素
	def getMin(self):
		if self.isEmpty("min"):
			return False
		else:
			return peek("min")

	# 返回栈顶元素
	def peek(self,key):
		map = {"data":self.data_items[-1],"min":self.data_items[-1]}
		return map[key]

	# 判断栈是否为空
	def isEmpty(self,key):
		map = {"data":self.data_size,"min":self.min_size}
		return map[key]


		