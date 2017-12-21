#-------------------------------回文判断------------------------------
#头尾扫描
def isPalindrome(pstring):
	n = len(pstring)
	start = 0
	last = n-1
	if n < 1:
		return False
	while start < last:
		if pstring[start] != pstring[last]:
			return False
		start += 1
		last -= 1
	return True

# 由中间开始扫描
def isPalindrome(pstring):
	n = len(pstring)
	if n < 1:
		return False
	elif n % 2 == 0:
		start,last = n//2-1, n//2
	else:
		start,last = n//2-1, n//2+1
	while start>=0:
		if pstring[start] != pstring[last]:
			return False
		start -= 1
		last += 1
	return True

#--------------------------------单向链表回文判断--------------------------------
#快慢指针找到中间节点->中间节点下一节点断开链表，反转链表->首尾依次对比
#definition for singly-linked list, 无头结点单链表
#class listnode:
#	def __init__(self,x):
#		self.value = x
#		self.next = None
#快慢指针查找中间节点
def findMid(head):
	fast = slow = head
	while (fast != None) and (fast.next != None) and (fast.next.next != None):
		fast = fast.next.next
		slow = slow.next
	return slow

#反转链表
def reverse(head):
	if head == None and head.next == None:
		return head
	newhead = reverse(head.next)
	head.next.next = head
	head.next = None
	return newhead

def isPalindrome(head):
	if head.next == None:
		return True
	pnow = findMid(head)
	split = pnow.next
	pnow.next = None #断开链表
	newhead = reverse(split)
	while (head != None) and (newhead != None):
		if head.value != newhead.value:
			return False
		head = head.next
		newhead = newhead.next
	return True





	






