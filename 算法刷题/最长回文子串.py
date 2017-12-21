#最长回文子串判断
#枚举所有回文子串法：扩展中心位置
def longestPalindrome(pstring):
	n = len(pstring)
	if n < 1:
		return n
	maxlen = 0
	index = 0
	for i in range(n):
		j = 0
		while (i-j)>=0 and (i+j)<n:#奇数长度
			if pstring[i-j] != pstring[i+j]:
				break
			c = 2*j + 1
			j += 1
		if c > maxlen:
			maxlen = c
			index = i - j + 1

		j = 0
		while (i-j)>=0 and (i+j+1)<n:#偶数长度
			if pstring[i-j] != pstring[i+j+1]:
				break
			c = 2*j + 2
			j += 1
		if c > maxlen:
			maxlen = c
			index = i - j + 1
	return maxlen, pstring[index:index+maxlen]

#Manacher算法
#解决长度奇偶性带来的对称轴问题 && 解决重复访问问题
def manacher(pstring):
	s = "#" + "#".join(pstring) + "#" #解决奇偶性问题
	n = len(s)
	rl = [0] * n   #记录第i个字符为对称轴的回文串的回文半径
	pos = 0        #记录最右侧回文子串中心的位置
	maxright = 0    #记录回文子串最右侧边界
	for i in range(n):
		if i < maxright:
			rl[i] = min(rl[2*pos-i],maxright-i)
		else:
			rl[i] = 1
		#扩展边界
		while (i - rl[i] >= 0) and (i + rl[i] < n) and (s[i-rl[i]] == s[i + rl[i]]):
			rl[i] += 1
		#更新最右侧回文子串信息
		if rl[i] + i - 1 > maxright:
			maxright = rl[i] + i - 1
			pos = i
	maxlen = max(rl) - 1
	index = (rl.index(maxlen+1) - 1) // 2
	return maxlen,pstring[index - (maxlen-1)//2:index - (maxlen-1)//2 + maxlen]

#动态规划法
#拆分为重叠子问题,依次划分为不同长度的子串，用数组记录是否为回文子串
'''状态转移方程：
dp[i][j]表示pstring[i]-psting[j]的子字符串是否为回文串
if i == j, dp[i][j] = True , 单个字符一定是回文数
if i-j == 1,dp[i][j] = (pstring[i]==psting[j]) 相邻字符串，比较两个字符
if i-j > 1,dp[i][j] = (pstring[i]==psting[j]) && (dp[i+1][j-1]) 长度大于1的字符串，根据两边界和子串判断
'''
#不要使用dp = [[0]*n]*n 生成矩阵
#重复操作符*,重复出来的各对象具有同一个id，也就是指向在内存中同一块地址，在对各个对象进行操作是一定要注意。
def palindromedp(pstring):
	n = len(pstring)
	dp = [[0] * n for i in range(n)] 
	maxlen = 0
	start = 0
	for length in range(n): #枚举子串长度
		for i in range(n-length):#枚举子串起始位置
			j = i + length 
			if i == j:
				dp[i][j] = 1
			elif (j == i + 1) and (pstring[i] == pstring[j]):
				dp[i][j] = 1
			elif (pstring[i] == pstring[j]) and (pstring[i+1] == pstring[j-1]):
				dp[i][j] = 1
			#更新最长子串信息
			if dp[i][j] and length > maxlen:
				maxlen = length
				start = i
	return maxlen+1, pstring[start:start+maxlen+1]









