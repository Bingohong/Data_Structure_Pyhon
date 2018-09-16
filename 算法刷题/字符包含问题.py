#字符串包含问题
#逐个对比 --- 时间复杂度O(m*n)
def stringContain(longstr,shortstr):
	a = len(longstr)
	b = len(shortstr)
	for i in range(b):
		j = 0
		while j < a and shortstr[i]!=longstr[j]:
			j += 1
		if j >= a:
			return False
	return True
		
#排序-轮询 --- 
def stringContain(longstr,shortstr):
	longstr = quicksort(longstr)
	shortstr = quicksort(shortstr)	a = len(longstr)
	b = len(shortstr)
	j = 0
	for i in range(b):
		found = False
		while j < a and not found:
			if shortstr[i] == longstr[j]:
				found = True
			else:
				j += 1
		if j >= a:
			return False
	return True

#素数整除法 --- 存在溢出问题
def stringContain(longstr,shortstr):
	repo = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 
	43, 47, 53, 59,61, 67, 71, 73, 79, 83, 89, 97, 101]
	a = len(longstr)
	b = len(shortstr)
	f = 1
	for j in range(a):
		x = repo[ord(longstr[j])-ord("A")]
		f *= x
	for i in range(b):
		x = repo[ord(shortstr[i])-ord("A")]
		if f % x:
			return False
	return True

#hashtable映射
# capital = [chr(i) for i in range(65,91)]
# repo = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 
# 43, 47, 53, 59,61, 67, 71, 73, 79, 83, 89, 97, 101]
# dic = dict(zip(capital,repo))


