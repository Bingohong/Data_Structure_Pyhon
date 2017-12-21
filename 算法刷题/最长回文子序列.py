#------------最长回文子序列问题(longest palindrome subsequence)---------
#反转字符串，转换为最长公共子序列问题(DP问题)
#最长公共子序列(longest common subsequence)
'''状态转移方程：
p[i,j]为字符串X前i个字符和字符串Y前j个字符的最长公共子序列长度
if i==0 or j==0, p[i][j]=0
if X[i]==Y[j], p[i][j]=p[i-1][j-1]+1
if X[i]!=Y[j], p[i][j]=max(p[i][j-1],p[i-1][j])
'''
def lps(pstring):
	preverse = pstring[::-1]
	n = len(pstring)
	dp = [[0] * (n+1) for i in range(n+1)]
	maxlen = 0
	for i in range(n):
		for j in range(n):
			if pstring[i] == preverse[j]:
				dp[i+1][j+1] = dp[i][j] + 1
			else:
				dp[i+1][j+1] = max(dp[i+1][j],dp[i][j+1])
			if maxlen < dp[i+1][j+1]:
				maxlen = dp[i+1][j+1]
	return maxlen,dp


#DP方法直接求解
'''分析：
对任意字符串，如果头和尾相同，那么它的最长回文子序列一定是去头去尾之后
的部分的最长回文子序列加上头和尾。如果头和尾不同，那么它的最长回文子序列
是去头的部分的最长回文子序列和去尾的部分的最长回文子序列的较长的那一个。
'''
'''状态转移方程：
p[i,j]为字符串S第i个字符到第j个字符的最长回文子序列长度
if i==j, p[i][j]=1
if i!=j,X[i]==Y[j], p[i][j]=p[i+1][j-1]+2
if i!=j,X[i]!=Y[j], p[i][j]=max(p[i+1][j],p[i][j-1])
'''
def lps(pstring):
	n = len(pstring)
	dp = [[0] * n for i in range(n)]
	maxlen = 0
	for length in range(n):#枚举子串长度
		for i in range(n-length):#枚举子串起始位置
			j = i + length
			if i == j:
				dp[i][j] = 1
			elif pstring[i] == pstring[j]:
				dp[i][j] = dp[i+1][j-1] + 2
			else:
				dp[i][j] = max(dp[i+1][j],dp[i][j-1])
			if dp[i][j] > maxlen:
				maxlen = dp[i][j]
	return maxlen,dp




