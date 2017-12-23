'''问题描述：由前序遍历序列和中序遍历序列重建二叉树'''
'''问题分析：
前序遍历可得到根节点，中序遍历可得到左右子树
由前序遍历和后序遍历，无法重建二叉树
1)根据前序遍历序列找到根节点
2)根据中序遍历结果划分左右子树
3)在左子树利用前序、中序特点找到根节点、左右子树
4)在右子树利用前序、中序特点找到根节点、左右子树
5)继续递归重建子树
'''
class binaryTree(object):
	"""docstring for binaryTree"""
	def __init__(self, value, left, right):
		self.value = value
		self.left = left
		self.right = right

def rebuild(preorder, inorder, length):
	if not preorder or not inorder or length == 0:
		return None
	
	value = preorder[0]
	root = binaryTree(value, None, None)

	for rootInorder in range(length):
		if value == inorder[rootInorder]:
			break
	if rootInorder == length:
		print("Invaild order!")
		return False
		

	leftTreeNode = rootInorder
	root.left = rebuild(preorder[1:1+rootInorder],inorder[:rootInorder], leftTreeNode)

	rightTreeNode = length - rootInorder - 1
	root.right = rebuild(preorder[1+rootInorder:], inorder[rootInorder+1:], rightTreeNode)
	
	return root

#前序遍历
def preorder(root):
	if root:
		print(root.value)
		preorder(root.left)
		preorder(root.right)

#中序遍历
def inorder(root):
	if root:
		inorder(root.left)
		print(root.value)
		inorder(root.right)

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

prelist = [1,2,4,5,3,6,7]
inlist = [4,2,5,1,6,3,7]
length = 7
root_ = rebuild(prelist, inlist, length)
