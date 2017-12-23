'''问题描述：求二叉树中两个节点的最近公共祖先节点'''
'''问题分析：
1)先序遍历
2)如果节点为空，返回空
3)如果节点为查找节点之一，返回该节点,标记为目标节点
4)如果节点不是两个节点之一，递归查找左右子树
5)如果该节点的左右子树含有查找节点，则该节点为最近祖先；
  否则返回左右子树中非空节点
'''

class binaryTree(object):
	"""docstring for binaryTree"""
	def __init__(self, value, left, right):
		self.value = value
		self.left = left
		self.right = right

def getLastCommonParent(root, node1, node2):
	# 空树，无对应的查找节点
	if root == None:
		return root

	# 节点为查找节点之一，返回该节点
	if root.value == node1.value or root.value == node2.value:
		return root
	
	# 查看左子树是否含有查找节点
	left = getLastCommonParent(root.left, node1, node2)
	# 查看右子树是否含有查找节点
	right = getLastCommonParent(root.right, node1, node2)
	
	# 如果左右子树都含有查找节点，则root为最近公共节点
	if left and right:
		return root

	# 返回左右子树中非空的节点
	return left or right

# 测试用例
root = binaryTree(1, None, None)

left = binaryTree(2, None, None)
right = binaryTree(3, None, None)
root.left = left
root.right = right

lleft = binaryTree(4, None, None)
lright = binaryTree(5, None, None)
rleft = binaryTree(6, None, None)
rright = binaryTree(7, None, None)
left.left = lleft
left.right = lright
right.left = rleft
right.right = rright

node1 = binaryTree(4,None,None)
node2 = binaryTree(5, None, None)

getLastCommonParent(root, node1, node2) # LCP -> node.value = 2