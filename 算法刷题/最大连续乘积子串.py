# ------------------------动态规划----------------------------
#---------------------最大连续乘积子串-----------------------
# 暴力轮询
def maxProductSubstring(alist):
	n = len(alist)
	maxresult = 0
	for i in range(n):
		temp = 1
		for j in range(i,n):
			temp *= j
			if temp>maxresult:
				maxresult = temp
	return maxresult

# DP方法-1
# 转移方程：maxend = max(maxend*a[i],a[i])
def maxProductSubstring(alist):
	n = len(alist)
	maxend = a[0]
	maxresult = a[0]
	for i in range(1,n):
		maxend = max(maxend * a[i], a[i])
		maxresult = max(maxresult, maxend)
	return maxresult

# DP方法-2
'''分析：
数组记录乘积，避免重复相乘
if j == i , dp[i][j] = a[j]
if j != i , dp[i][j] = dp[i][j-1]*a[j]
'''
def maxProductSubstring(alist):
	n = len(alist)
	dp = [[0] * n for i in range(n)]
	maxresult = a[0]
	for i in range(n):
		for j in range(i,n):
			if i == j :
				dp[i][j] = a[j]
			else:
				dp[i][j] = dp[i][j-1]*a[j]
			if maxresult < dp[i][j]:
				maxresult = dp[i][j]
	return maxresult