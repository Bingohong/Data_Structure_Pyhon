# 杨氏矩阵查找
# ------------------定位法，线性查找时间复杂度O(m+n)-------------
'''分析：
直接定位到最右上角的元素
比要找的数大就往左走
比要找数的小就往下走
直到找到要找的数字（6）为止
'''
def young_matrix(matrix,item):
	m, n = len(matrix), len(matrix[0])
	i, j = 0, n-1
	while j>=0 and i<m:
		if matrix[i][j] == item:
			return (i,j)
		elif matrix[i][j] < item:
			j -= 1
		elif matrix[i][j] > item:
			i += 1
	return -1

# -----------------------------分治法，递归查找---------------------
'''分析：
矩阵中间元素将矩阵分为4个子块：leftup,leftdown,rightup,rightdown
if item > leftup[-1][-1],排除leftup子块,搜索其余3块
if item < rightdown[0][0],排除rightdown子块，搜索其余3块
'''
def young_matrix(matrix,item):
	m, n = len(matrix), len(matrix[0])
	if m==0 or n==0:
		return False
	elif item<matrix[0][0] or item>matrix[-1][-1]:
		return False
	elif item==matrix[0][0] or item==matrix[-1][-1]:
		return True
	leftup = matrix[0:m//2,0:n//2]
	leftdown = matrix[m//2:,0:n//2]
	rightup = matrix[0:m//2,n//2:]
	rightdown = matrix[m//2:,n//2:]
	bound1 = leftup[-1][-1]
	bound2 = rightdown[0][0]
	ret = young_matrix(rightup,item) or young_matrix(leftdown,item)
	if bound1>=item:
		return young_matrix(leftup,item) or ret
	elif key>bound1 and key<bound2:
		return ret
	else:
		return young_matrix(rightdown,item) or ret
