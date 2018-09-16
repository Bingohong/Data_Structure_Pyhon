'''问题描述：
输入一个整数数组,判断该数组是不是某二元查找树的后序遍历的结果。
'''
'''问题分析：
最主要的性质就是左子树的任何节点都小于根节点，右子树的任何节点都大于根节点。
后序遍历的最后一位肯定是根节点
1) 序列的最后一位a[n-1]必定是根节点
2) 前面的序列中连续一部分是左子树的遍历
3) 另一部份是右子树的遍历
此时需要在前面的序列中查找第一个大于root的节点a[i]
'''
def isPostOrder(alist, splitpoint):
	if not alist and splitpoint <= 0:
		return False

	root = splitpoint - 1

	# 寻找第一个大于root节点的值
	i = 0
	while alist[i] < alist[root] and i < root:
		i += 1

	# 判断右侧是否满足大小关系
	for j in range(i,root):
		if alist[j] < alist[root]:
			return False
	
	# 左子树长度大于0，递归左子树
	left = True
	if i > 0:
		left = isPostOrder(alist[:i], i)

	# 右子树长度大于0， 递归右子树
	right = True
	if i < root:
		right = isPostOrder(alist[i:root], root-i)

	return (left & right)

# 测试代码
alist = [5,7,6,9,11,10,8] #true
blist = [7,4,6,5] # false
