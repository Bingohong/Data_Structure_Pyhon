#矩阵相乘问题
#暴力相乘法
def matrixDot(A,B):
	m = len(A) #A的行
	n = len(A[0]) #A的列
	p = len(B[0]) #B的列
	C = [[0] * m for i in range(p)]
	for i in range(m):
		for k in range(p):
			C[i][k] = 0
			for j in range(n):
				C[i][k] += A[i][j] * B[j][k]
	return C

#Strassen算法---时间复杂度O(n^2.807)
#Coppersmith–Winograd算法---时间复杂度O(n^2.3754)
#Andrew Stothers---时间复杂度O(n^2.3736)
#Virginia Williams---时间复杂度O(n^2.3727)
