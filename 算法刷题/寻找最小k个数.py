#寻找最小K个数---快速选择(类似于快速排序)
def quickselection(alist,k,first,last):
	splitpoint = partition(alist,first,last)
	if splitpoint == k-1:
		return splitpoint
	elif splitpoint > k-1: # 分裂点左侧数目大于k个数时，递归分裂点左侧列表，递归数量为k
		quickselection(alist,k,first,splitpoint)
	else: # 分裂点左侧数目小于k个数时，递归分裂点右侧列表，递归数量为k-(splitpoint+1)
		quickselection(alist,k-1-splitpoint,splitpoint+1,last)

def partition(alist,first,last):
	pivot = alist[first]

	leftmark = first + 1
	rightmark = last - 1
	done = False

	while not done:
		while leftmark<=rightmark and alist[leftmark]<=pivot:
			leftmark += 1
		while leftmark<=rightmark and alist[rightmark]>=pivot:
			rightmark -=1
		if leftmark <= rightmark:
			alist[leftmark],alist[rightmark] = alist[rightmark],alist[leftmark]
		else:
			done = True
	alist[first],alist[rightmark] = alist[rightmark],alist[first]
	return rightmark

#二叉堆中的最大堆实现
'''分析：
根节点为最大值kmax
if x<kmax，替换kmax
下沉节点数值，保持堆次序
'''