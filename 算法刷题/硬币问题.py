# --------------------------硬币问题--------------------------
# 递归法
'''分析：
一个1分钱加上原始金额减去1分钱所需的硬币数量
一个 5 美分加上原始金额减去 5 美分所需的硬币数量
一个 10 美分加上原始金额减去 10 美分所需的硬币数量
'''
def recMakeChange(coinValueList,change):
	minCoins = change 
	if change in coinValueList:
		return 1
	else:
		for i in [c for c in coinValueList if c <= change]:
			numCoins = 1 + recMakeChange(coinValueList,chang-i)
			if numCoins < minCoins:
				minCoins = numCoins
	return minCoins

# 动态规划法
'''分析：完全背包问题
minCoins[i][cents] = 前i个硬币对零钱j得到的最少硬币数量
第一列minCoins[i][0] = 零钱0，认为随时都可以满足但数量为空 = 0
第一行minCoins[0][1:end] = 硬币价值为0，永远不可能找零 = NULL
不限制硬币数量，使用同一行或正上方结果
if c[i]<=cents, 选择同一行，minCoins[i][cents-c[i]]
if c[i]>cents, 选择正上方, minCoins[i-1][cents]或cents
'''
def dpMakeChange(coinValueList,change):
	n = len(coinValueList)
	minCoins = [[0] * (change+1) for i in range(n)]
	for i in range(n):
		for cents in range(1,change+1):
			if i == 0:
				minCoins[i][cents] = None
			elif coinValueList[i] > cents:
				a = minCoins[i-1][cents]
				if a == None:
					minCoins[i][cents] = cents
				else:
					minCoins[i][cents] = a
			else:
				minCoins[i][cents] = minCoins[i][cents-coinValueList[i]] + 1
	return minCoins

# 空间优化
def dpMakeChange(coinValueList,change):
	minCoins = [0] * (change+1)
	for cents in range(change+1):
		coinCount = cents
		for j in [c for c in coinValueList if c <= cents]:
			if minCoins[cents-j] < coinCount:
				coinCount = minCoins[cents-j] + 1
		minCoins[cents] = coinCount
	return minCoins