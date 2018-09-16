#荷兰国旗问题(Dutch National Flag Problem)
#三色小球有序排列后正好分为三类
#分治思想，类似快速分类
'''分析：
设定三个指针，前指针begin,尾指针end，遍历指针current
if current == 0 ,swap(alist[begin],alist[current]),begin++,current++
if current == 1 ,current++
if current == 2 ,swap(alist[current],alist[end]),end--
尤其注意此时current保持不变，因为当end指向0时，
交换后current就会指向0，此时若是current++，就会漏判情况1
'''
def dutchFlag(alist):
	n = len(alist)
	begin = 0
	end = n - 1
	current = 0
	while(current<=end):
		if alist[current] == 0:
			alist[current],alist[begin] = alist[begin],alist[current]
			current += 1
			begin += 1
		elif alist[current] == 1:
			current += 1
		else:
			alist[end],alist[current] = alist[current],alist[end]
			end -= 1
	return alist
