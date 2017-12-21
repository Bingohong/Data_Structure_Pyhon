#--------------------最长公共子串/子序列问题--------------
def lcsubstring(s1, s2):
	matrix = [[0] * (len(s2) + 1) for i in range(len(s1)+1)]

	mmax = 0
	p = 0 #最长匹配对应在s1的最后一位
	for i in range(len(s1)):
		for j in range(len(s2)):
			if s1[i] == s2[j]:
				matrix[i+1][j+1] = matrix[i][j] + 1
				if mmax < matrix[i+1][j+1]:
					mmax = matrix[i+1][j+1]
					p = i + 1
	return s1[p-mmax:p], mmax


def lcsubsequence(s1, s2):
	matrix = [[0] * (len(s2) + 1) for i in range(len(s1)+1)]
	# 记录转移方向，便于回溯
	driver = [[None] * (len(s2) + 1) for i in range((len(s1) + 1))]

	for i in range(len(s1)):
		for j in range(len(s2)):
			if s1[i] == s2[j]:
				matrix[i+1][j+1] = matrix[i][j] + 1
				driver[i+1][j+1] = "ok"
			else:
				matrix[i+1][j+1] = max(matrix[i+1][j], matrix[i][j+1])
				if matrix[i+1][j+1] == matrix[i+1][j]:
					driver[i+1][j+1] = "left"
				else:
					driver[i+1][j+1] = "up"
	
	(p1, p2) = (len(s1), len(s2))
	s = [] #记录回溯子序列
	while matrix[p1][p2]:#不为None时
		record = driver[p1][p2]
		if record == "ok":         #匹配成功，插入该字符，并向左上角找下一个
			s.append(s1[p1-1])
			p1 -= 1
			p2 -= 1
		if record == "left":       #根据标记，向左找下一个
			p2 -= 1
		if record == "up":         #根据标记，向上找下一个
			p1 -= 1
	s.reverse()

	return "".join(s),matrix,driver


