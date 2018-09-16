'''问题描述：判断两棵二叉树是否结构相同'''
'''问题分析：
1)先序遍历
2)如果二叉树都为空，True
3)如果二叉树一棵为空，另一棵非空，False
4)两棵树的左右子树同时递归
'''
class binaryTree(object):
	"""docstring for binaryTree"""
	def __init__(self, value, left, right):
		self.value = value
		self.left = left
		self.right = right

def cmpStructure(root1, root2):
	if root1 == None and root2 == None:
		return True 
	elif root1 == None or root2 == None:
		return False 

	left = cmpStructure(root1.left, root2.left)
	right = cmpStructure(root1.right, root2.right)
	return left and right

# 测试用例
root1 = binaryTree(1, None, None)

left = binaryTree(2, None, None)
right = binaryTree(3, None, None)
root1.left = left
root1.right = right

lleft = binaryTree(4, None, None)
lright = binaryTree(5, None, None)
rleft = binaryTree(6, None, None)
rright = binaryTree(7, None, None)
left.left = lleft
left.right = lright
right.left = rleft
right.right = rright

root2 = binaryTree(1, None, None)

left = binaryTree(2, None, None)
right = binaryTree(3, None, None)
root2.left = left
root2.right = right

lleft = binaryTree(4, None, None)
lright = binaryTree(5, None, None)
left.left = lleft
left.right = lright

cmpStructure(root1,root2) # False

