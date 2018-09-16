# 牛客网输入
# 1.多行输入
import sys
while True:
	try:
		n = int(sys.stdin.readline())
		print(n)
	except:
		break

# 2.去除最后的换行符号,读入的字符串中有\n,python本身的字符串中没有
sys.stdin.realine() # 读入一行字符串
sys.stdin.realine().strip() # 去除最后的换行符号\n
sys.stdin.realine().split() # 分割为列表