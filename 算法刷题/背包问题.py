#------------------背包问题-------------------------
'''分析：
t[i][j] = 前i件商品在j空间得到的最大价值
'''
'''测试用例
n = 3
c = [None, 3,4,5]
v = [None, 4,5,6]
totalC = 10
'''
def zeroOne(n,totalC,c,v):
	t = [[0] * (totalC + 1) for i in range(n+1)]
	for i in range(1, n+1):
		for j in range(1,totalC+1):
			if c[i] > j:
				t[i][j] = t[i-1][j]
			else:
				t[i][j] = max(t[i-1][j], t[i-1][j-c[i]] + v[i])
	return t

# 求最大价值时的物品选择方案
t = zeroOne()
# print path 方法1
i = n
j = totalC
while i > 0 and j > 0:
    if t[i][j] != t[i-1][j]:    # 选了第i个物品
        print ("第%s个物品, 空间：%s, 价值：%s" % (i,c[i],v[i]))
        j -= c[i]
    # 考察前一个物品
    i -= 1

# ---------------------恰好装满--------------------------
'''分析：
第一列f[i][0] = 背包空间为0，认为永远是满的，且无法放物品 = 0
第一行f[0][1:end] = 没有物品可放，除空间为0背包，其他背包永远不可能放满 = NULL
'''
def zeroOneFull(n, totalC, c, v):
	t = [[0] * totalC for i in range(n)]
	for i in range(n+1):
		for j in range(totalC+1):
			if i == 0 and j > 0:
				t[i][j] = None
			elif c[i] > j:
				t[i][j] = t[i-1][j]
			else:
				a = t[i-1][j-c[i]]
				b = t[i-1][j]

				if a != None and b!= None:
					t[i][j] = max(b,a+v[i])
				elif a == None and b == None:
					t[i][j] = None
				elif a != None and b == None:
					t[i][j] = a + v[i]
				else:
					t[i][j] = b

#-----------------空间优化策略----------------------------------
def zeroOne2(n,totalC,c,v):
	t = [0] * (totalC + 1)
	path = [[0] * (totalC + 1) for i in range(n+1)]

	for i in range(1, n+1):
		for j in reversed(range(c[i],totalC+1)):#从右至左递推
			t[j] = max(t[j], t[j-c[i]] + v[i])
			# 如果选择了第i个物品，记录path
			if t[j] == t[j-c[i]] + v[i]:
				path[i][j] = 1

	return t,path

# 求最大价值时的物品选择方案
t,path = zeroOne2()
i = n
j = totalC
while i > 0 and j > 0:
    if path[i][j] == 1: # 选了第i个物品 
        print ("第%s个物品，空间：%s，价值：%s" % (i,c[i],v[i]))
        j -= c[i]
    i -= 1