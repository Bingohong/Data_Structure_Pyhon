'''问题描述：判断二叉树是不是完全二叉树'''
'''问题分析：
1)层序遍历
2)完全二叉树，每层达到最大节点数2^(h-1),除第h层外，第h层必须全部为叶子节点
3)除叶子节点外，每个节点必须是左子树为非空，右子树为空
4)从出现空子树的节点开始，其后必须都为叶子节点
'''
class binaryTree(object):
	"""docstring for binaryTree"""
	def __init__(self, value, left, right):
		self.value = value
		self.left = left
		self.right = right

def isCompleteBinaryTree(rook):
	if root == None:
		return False

	queue = []
	queue.insert(0,root)
	result = True
	mustHaveNoChild = False #为True时说明后续遍历的节点都应为叶子节点

	while queue != []:
		node = queue.pop()
		# 为True时，后续节点应为叶子节点
		if mustHaveNoChild:
			# 出现非叶子节点，则不是完全二叉树
			if node.left != None or node.right != None:
				result = False
				break
		else:
			if node.left and node.right: # 左右子树都存在，入队
				queue.insert(0,node.left)
				queue.insert(0,node.right)
			elif not node.left and not node.right: # 左右节点都为空
				mustHaveNoChild = True
			elif node.left and not node.right: # 左子树存在，右子树空
				mustHaveNoChild = True
				queue.insert(0,node.left)
			else: #　左子树空，右子树存在，不是完全二叉树
				result = False
				break
	return result

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

isCompleteBinaryTree(root) # True

