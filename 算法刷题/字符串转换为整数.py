#字符串转换为整数
#溢出问题的处理
def strtoint(strnum):
	up = int((2**32-1)/2)
	down = -int(2**32/2)
	s = len(strnum)
	if s == 0:
		return 0
	elif strnum[0]=="-":
		sign = -1
		strnum = strnum[1:]
	elif strnum[0]=="+":
		sign = 1
		strnum = strnum[1:]
	else:
		sign = 1

	f = 0
	for i in range(s):
		n = int(strnum[i])
		if sign>0 and ((f>up//10) or ((f==up//10) and f>(up%10))):
			return up
		elif sign<0 and ((f>down//10) or ((f==down//10) and f>(down%10))):
			return down
		f = f*10 + n
	return f*sign
