#------------------------------树遍历-----------------------------------
class binaryTree(object):
	"""docstring for binaryTree"""
	def __init__(self, value, left, right):
		self.value = value
		self.left = left
		self.right = right

#前序遍历
def preorder(root):
	if root:
		print(root.value())
		preorder(root.left())
		preorder(root.right())

#中序遍历
def inorder(root):
	if root:
		inorder(root.left())
		print(root.value())
		inorder(root.right())

#后序遍历
def postorder(root):
	if root != None:
		postorder(root.left())
		postorder(root.right())
		print(root.value())

#分层遍历
'''分析：
1)相当于广度优先搜索，使用队列结构
2)队列初始化，根节点压入队列
3)当队列不为空，进行如下操作：
	3.1)弹出一个节点，访问
	3.2)若左子节点或右子节点不为空，将其压入队列。
'''
def hierarchyOrder(root):
	if root == None:
		return 0
	queue = []
	queue.insert(0,root)

	while queue != []:
		node = queue.pop()
		
		if node.left:
			queue.insert(0,node.left)
		if node.right:
			queue.insert(0,node.right)

		print([i.value for i in queue])
	return