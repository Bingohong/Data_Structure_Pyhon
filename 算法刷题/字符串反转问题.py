#-------------------------字符串问题---------------------
#旋转字符串
#1.brute force --- 时间复杂度O(n*n),空间复杂度O(1)
def rotateString(str,m):
	n = len(str)
	for i in range(m):
		t = str[0]
		for j in range(1,n):
			str[j-1] = str[j]
		str[n-1] = t
	return str

#2.三步反转法 --- (X^TY^T)^T=YX
def reverseString(str,start,end):
	while start < end:
		str[start],str[end] = str[end] ,str[start]
		start += 1
		end -= 1
def ratateString(str,m):
	n = len(str)
	m %= n
	reverseString(str,0,m-1)
	reverseString(str,m,n-1)
	reverseString(str,0,n-1)

#3.内建函数
def ratateString(string):
	s = string.split(" ")
	return " ".join(s[::-1])