# 交替字符串问题
''' 问题描述：
输入三个字符串s1、s2和s3，判断第三个字符串s3是否由前两个字符串s1和s2交错而成，
即不改变s1和s2中各个字符原有的相对顺序，
例如当s1 = “aabcc”，s2 = “dbbca”，s3 = “aadbbcbcac”时，则输出true，
但如果s3=“accabdbbca”，则输出false。
'''
'''分析：
dp[i][j]表示s3[i+j-1]是否为s1[i-1]和s2[j-1]交替组成的记忆搜索矩阵
即dp[i-1][j]表示s3[i+j-2]是否为s1[i-2]和s2[j-1]交替组成
n=len(s1), m=len(s2); 取i=[0,n], j=[0,m], i=0 j=0做为边界(空串)
if i==0 or j==0, dp[i][j]=1, 初始化边界：空串可以由空串组成
if s1[i-1] == s3[i+j-1] and dp[i-1][j], dp[i][j]=1
if s2[j-1] == s3[i+j-1] and dp[i][j-1], dp[i][j]=1
'''
def isInterleave(s1,s2,s3):
	n = len(s1)
	m = len(s2)
	dp = [[0] * (1+m) for i in range(1+n)]
	for i in range(n+1):
		for j in range(m+1):
			if i==0 or j==0:
				dp[i][j] = True
			elif s1[i-1] == s3[i+j-1] and dp[i-1][j]:
				dp[i][j] = True
			elif s2[j-1] == s3[i+j-1] and dp[i][j-1]:
				dp[i][j] = True
			else:
				dp[i][j] = False
	return dp,dp[-1][-1]