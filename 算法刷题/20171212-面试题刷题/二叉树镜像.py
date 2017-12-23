'''问题描述：二叉树的镜像'''
'''问题分析：
1)先序遍历
2)如果二叉树为空，返回节点
3)如果二叉树非空，交换左右子树节点
4)递归左子树、右子树
'''
class binaryTree(object):
	"""docstring for binaryTree"""
	def __init__(self, value, left, right):
		self.value = value
		self.left = left
		self.right = right

def mirrorTree(root):
	if root == None:
		return root

	root.left, root.right = root.right, root.left

	mirrorTree(root.left)
	mirrorTree(root.right)

	return root

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

mirrorTree(root)

