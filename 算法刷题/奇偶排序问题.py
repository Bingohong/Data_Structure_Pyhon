#奇偶排序问题
#快速排序法类似
'''分析：
一头一尾双端指针扫描，头指针指向奇数，尾指针指向偶数
当头指针指向偶数且尾指针指向奇数时，交换数字
'''
def oddevenSort(alist):
	n = len(alist)
	leftmark = 0
	rightmark = n - 1
	while leftmark < rightmark:
		if (alist[leftmark]&1 == 1):
			leftmark += 1
		elif (alist[rightmark]&1 != 1):
			rightmark -= 1
		else:
			alist[leftmark],alist[rightmark] = alist[rightmark],alist[leftmark]
	return alist

