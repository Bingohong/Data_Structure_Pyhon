# 递归算法实例-hannuo tower
def mov(n,a,b,c):
	if n==1:
		print(a,"->",c)
	else:
		mov(n-1,a,c,b) %移动上部n-1个盘子从a->b
		mov(1,a,b,c)   %移动第n个盘子
		mov(n-1,b,a,c) %移动下部n-1个盘子从b->c

# 递归算法实例-factorial
def factorial(n):
	if n<=1:
		return 1
	else:
		return n * factorial(n-1)

# 递归进制转换
def to_str(n,base):
	convert_string = "0123456789ABCDEF"
	if n < base:
		return convert_string[n]
	else:
		return to_str(n//base, base) + convert_string[n%base]
