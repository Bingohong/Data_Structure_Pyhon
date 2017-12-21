'''问题描述：求二叉树中节点个数'''
'''问题分析：
1)后序遍历
2)如果二叉树为空，节点个数为0
3)如果二叉树不为空，二叉树节点个数 = 左子树节点个数 + 右子树节点个数 + 1
'''
class binaryTree(object):
	"""docstring for binaryTree"""
	def __init__(self, value, left, right):
		self.value = value
		self.left = left
		self.right = right

def getTreeNode(root):
	if root == None:
		return 0

	left = getTreeNode(root.left)
	right = getTreeNode(root.right)

	return left + right + 1

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

getTreeNode(root) # node_number = 7

