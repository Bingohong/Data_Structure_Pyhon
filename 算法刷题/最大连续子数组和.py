#最大连续子数组和
#暴力枚举法---时间复杂度O(n^3)
def maxSubArray(alist):
	currSum = 0
	maxSum = alist[0]
	n = len(alist)
	for i in range(n-1):#控制起点
		for j in range(i+1,n):#控制终点
			for k in range(i,j):#求和
				currSum += alist[k]
			if currSum > maxSum:
				maxSum = currSum
				start = i
				end = j
			currSum = 0
	return maxSum,alist[start:end+1]

def maxSubArray(alist):
	maxSum = alist[0]
	n = len(alist)
	for i in range(n):#控制起点
		currSum = 0
		for j in range(i,n):#控制终点
			currSum += alist[j]
			if currSum > maxSum:
				maxSum = currSum
	return maxSum

#数组筛选法
'''分析：
对第j+1个元素有两种选择：要么放入前面找到的子数组，要么做为新子数组的第一个元素；
如果currSum加上当前元素a[j]后不小于a[j]，则令currSum加上a[j]，否则currSum重新赋值，置为下一个元素，即currSum = a[j]。
同时，当currSum > maxSum，则更新maxSum = currSum，否则保持原值，不更新。
'''
def maxSubArray(alist):
	currSum = 0
	maxSum = 0
	n = len(alist)
	record = [0] * n
	for i in range(n):
		temp = currSum + alist[i]
		if temp >= alist[i]:
			currSum = temp
			record[i] = 1
		else:
			currSum = alist[i]
			record = [0] * n
			record[i] = 1
		if currSum > maxSum:
			maxSum = currSum
			maxrecord = record.copy()
	return maxSum,maxrecord
