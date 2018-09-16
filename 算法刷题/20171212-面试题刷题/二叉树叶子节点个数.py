'''问题描述：求二叉树中叶子节点的个数'''
'''问题分析：递归解法
1)先序遍历
2)如果二叉树为空,返回0
3)如果二叉树无左右子树，返回1
4)如果二叉树不为空且含有子树，递归
同求二叉树第K层的节点个数方法一致，更改递归基准条件即可
'''
class binaryTree(object):
	"""docstring for binaryTree"""
	def __init__(self, value, left, right):
		self.value = value
		self.left = left
		self.right = right

def getLeafNode(root,k):
	if root == None:
		return 0

	if (not root.left) and (not root.right): 
		return 1

	left = getHierarchyNode(root.left)
	right = getHierarchyNode(root.right)

	return left + right

# ------------------------------------------------------------------
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

k = 2
getHierarchyNode(root,k) # nodenum = 2

