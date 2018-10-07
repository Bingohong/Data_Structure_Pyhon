'''题目：剑指offer39题，输入一颗二叉树的根节点，判断该树是否为平衡二叉树
解题思路：后序遍历方式，记录每个结点的深度
'''
def isBalanced(root):
  if not root:
    depth = 0
    # 需要返回当前结点深度和是否平衡
    return depth, True　
  
  # 返回值有两个，都要记录
  left, lbool = isBalanced(root.left)
  right, rbool = isBalanced(root.right)
  print("root-value %d, left %d, right %d"%(root.value, left, right))
  
  # 先遍历的结点满足平衡条件时，继续
  if lbool and rbool:
    diff = left - right
    print("diff height %d"%(diff))
    # 不要使用or，会发生惰性运算
    # 若diff==2，则diff<=1为False，然后继续判断diff>=-1为True，显然不正确
    if diff<=1 and diff>=-1:
      depth = max(left,right) + 1 # 更新当前深度
      return depth, True
  
  return max(left, right)+1 , False

#　测试
class binaryTree(object):
	"""docstring for binaryTree"""
	def __init__(self, value, left, right):
		self.value = value
		self.left = left
		self.right = right
    
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
