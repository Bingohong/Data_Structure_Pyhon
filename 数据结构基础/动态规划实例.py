# 动态规划算法实例

# ----------------------最大乘积问题--------------------------
#有问题
def dpProduct(N):
	product = [0] * (N + 1)
	for number in range(1,N+1):
		maxProduct = 0
		for i in range(number):
			if product[number-i] * i > maxProduct:
				maxProduct = product[number-i] * i
		product[number] = maxProduct
	return product[N]

#--------    -------------数塔问题----------------------------
def tower_walk(data,n):
	from copy import deepcopy
	dp = deepcopy(data)#深层复制
	record = []
	for i in reversed(range(n-1)):
		for j in range(i+1):
			temp_max = max(dp[i+1][j], dp[i+1][j+1])
			dp[i][j] = temp_max + data[i][j]
		if temp_max == dp[i+1][j]:#记录路径，自底向上
			record.append(data[i+1][j])
		else:
			record.append(data[i+1][j+1])
	record.append(data[0][0])
	return dp,record




