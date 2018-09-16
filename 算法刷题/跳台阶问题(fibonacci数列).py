#跳台阶问题(fibonacci数列)
#递推法
def fibonacci(n):
	fib = [1,1,2]
	if n < 2:
		return 1
	for i in range(2,n+1):
		fib[2] = fib[0] + fib[1]
		fib[0] = fib[1]
		fib[1] = fib[2]
	return fib[2]

#递归法
def fibonacci(n):
	if n < 2:
		return 1
	return fibonacci(n-1) + fibonacci(n-2)
