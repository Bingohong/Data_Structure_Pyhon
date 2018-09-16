'''问题描述：在二元树中找出和为某一值的所有路径
输入一个整数和一棵二元树。
从树的根结点开始往下访问一直到叶结点所经过的所有结点形成一条路径。
打印出和与输入整数相等的所有路径。
'''
'''分析：
二叉树的先序遍历
栈结构保存根节点值
路径与递归调用栈一致，递归过程也是个出栈&入栈过程
'''
'''思路：
前序遍历访问某一结点，将该结点压入栈中，并累加该结点的值。
若该结点为叶结点且栈中结点值和刚好为输入的整数， 则当前的路径符合要求，我们把它打印出来。
如果当前结点不是叶结点，则继续访问它的子结点。
当前结点访问结束后，递归函数将自动回到它的父结点。
函数退出之前要在栈中删除当前结点并减去当前结点的值，以确保返回父结点时路径刚好是从根结点到父结点的路径
'''

class treeNode(object):
	"""docstring for treeNode"""
	def __init__(self, value=None, left=None, right=None):
		super(treeNode, self).__init__()
		self.value = value
		self.leftchild = left
		self.rightchild = right

def findPath(expectedSum, tree, curSum=0, stack=[]):
	if tree:
		# 先处理根节点
		curSum += tree.value
		stack.append(tree.value)
		if curSum < expectedSum: # 递归条件
			# 递归左子树
			findPath(expectedSum, tree.leftchild, curSum=curSum, stack=stack)
			# 递归右子树
			findPath(expectedSum, tree.rightchild, curSum=curSum, stack=stack)
		elif curSum == expectedSum: # 基线条件
			# 当前为根节点，这输出结果
			if not tree.leftchild and not tree.rightchild:
				print(stack)
		# 栈结构与递归过程保持一致，递归结束时要将该层节点值弹出
		stack.pop()
	

# 测试用例
pNode1 = treeNode(10)
pNode2 = treeNode(5)
pNode3 = treeNode(12)
pNode4 = treeNode(4)
pNode5 = treeNode(7)

pNode1.leftchild = pNode2
pNode1.rightchild = pNode3
pNode2.leftchild = pNode4
pNode2.rightchild = pNode5

def show(tree):
	if tree:
		print(tree.value)
		show(tree.leftchild)
		show(tree.rightchild)

findPath(22, pNode1)