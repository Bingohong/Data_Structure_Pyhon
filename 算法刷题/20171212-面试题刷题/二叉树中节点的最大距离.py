'''问题描述：
求二叉树中节点的最大距离
如果把二叉树看成一个图，父子节点之间的连线看成是双向的，
定义“距离”为两个节点之间边的个数。
'''
'''问题分析：
后序遍历方法遍历节点
二叉树中节点的最大距离为两个叶子节点的距离。
求某个子树的节点的最大距离，有三种情况：
1) 若根节点无右子树，则两个叶子节点都出现在左子树；
2) 若根节点无左子树，则两个叶子节点都出现在右子树；
3) 若根节点左右子树健全，则一个叶子节点在左子树，一个叶子节点在右子树。
只要求得三种情况的最大值，结果就是这个子树的节点的最大距离。
'''

class binaryTree(object):
	"""docstring for binaryTree"""
	def __init__(self, value, left, right):
		self.value = value
		self.left = left
		self.right = right

def find_max_len(root):
	if root == None:
		return 0
	print(root.value)
	# 左子树最大值
	leftmax = find_max_len(root.left)
	print(leftmax)
	# 右子树最大值
	rightmax = find_max_len(root.right)
	print(rightmax)

	leftlen = height(root.left) # 求root节点的左子树高度
	print(leftlen)

	rightlen = height(root.right) # 求root节点的右子树高度
	print(rightlen)

	return max(max(leftmax, rightmax), leftlen+rightlen) 

def height(root):
	if root == None:
		return 0
	print(root.value)
	return max(height(root.left), height(root.right)) + 1
		

# 测试用例，一棵完全二叉树
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

find_max_len(root) # max_len = 4