'''问题描述：求二叉树第K层的节点个数'''
'''问题分析：递归解法
1)先序遍历
2)如果二叉树为空或者k<1,返回0
3)如果二叉树不为空并且k==1，返回1
4)如果二叉树不为空且k>1，返回左子树中k-1层的节点个数与右子树k-1层节点个数之和
计算k-1层节点个数，原因:
当二叉树递归进入下一层时，相当于当前树深度少一层；
这种计算节点的思路是想最终递归至K目标层，此时递归函数内k=1。
第k层的节点数量 = 第k层产生的递归函数数目
'''
class binaryTree(object):
	"""docstring for binaryTree"""
	def __init__(self, value, left, right):
		self.value = value
		self.left = left
		self.right = right

def getHierarchyNode(root,k):
	if root == None or k < 1:
		return 0
	if k == 1:
		return 1

	left = getHierarchyNode(root.left, k-1)
	right = getHierarchyNode(root.right, k-1)

	return left + right

# -----------------------------------------------------------------
'''问题分析：非递归解法-队列
按层次计算，逐层遍历每层的节点数目
关键在于保证计算第k层节点数目时，前面k-1层节点完全出队列
1)层次遍历，节点入队列
2)计算当前层节点数目，即队列长度
3)依据队列长度，执行出队、入队操作
4)执行完3)后即可动态地保持当前队列长度为当前层节点数目
'''
def getHierarchyNode(root,k):
	if root == None or k < 1:
		return 0

	curLevelNode = 0 # 记录当前层节点数目
	curLevel = 0 #记录当前层次

	queue = []
	queue.insert(0, root)

	while queue != []:
		curLevel += 1 
		curLevelNode = len(queue) #计算当前队列长度

		if curLevel == k:
			break

		temp_count = 0
		while temp_count < curLevelNode: #依据队列长度执行出队
			temp_count += 1
			node = queue.pop()
			if node.left:
				queue.insert(0, node.left)
			if node.right:
				queue.insert(0, node.right)
	
	while queue != []: #清空队列
		queue.pop()

	if curLevel == k:
		return curLevelNode

	return 0

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

