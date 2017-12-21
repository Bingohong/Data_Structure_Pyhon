# 递推算法实例-顺推法-斐波那契数列 
def Fibonacci_sequence(NUM = 13)
	fib = [1,1]
	for i in range(2,NUM):
		temp = fib[i-1] + fib[i-2]
		fib.append(temp)
		print("第%d个数的Fibonacci数列为%d" %(i,fib[i]))
	return fib

# 递推算法实例-逆推法-银行存款问题
def Bank_deposit(FETCH = 1000):
	FETCH = 1000
	rate = 0.0171
	period = 48
	deposit = [0]
	for i in range(period):
		temp = (deposit[i] + FETCH)/(1 + rate/12)
		deposit.append(temp)
		print("第%d个月还有存款%.2f元" %((period-i),deposit[i]))

