#链表反转
#definition for singly-linked list
#class listnode:
#	def __init__(self,x):
#		self.value = x
#		self.next = None

class solution(object):
	"""docstring for solution"""
	#非递归实现
	def reverselist(self, head):
		prev = None # 链表断裂，记录previous/current/next-Node信息
		curr = head
		while curr is not None:
			pnext = curr.next
			curr.next = prev
			prev = curr
			curr = pnext
		head = prev

		return head

	#递归实现
	def reverse(self,head):
		if head is None or head.next is None:
			return head
		newhead = self.reverse(head.next) # newhead为记录的新头结点位置
		head.next.next = head #反转头结点和相邻节点
		head.next = None      #头结点的下一节点置空
		return newhead
