#-----------------寻找和为定值的若干个数--------------------
#和为定值的两个数
'''分析：
方法一：有序数组，对于每个a[i],查找sum-a[i]是否在数组中，二分查找，时间复杂度O(nlogn)
方法二：扫描sum-a[i],参看两个数组是否有相数值
方法三：有序数组，双端指针逼近 if a[i]+a[j]>sum, j--;if a[i]+a[j]<sum,i++，时间复杂度O(n)
'''
#双端逼近
def twosum(alist,sumnum):
	left = 0
	right = len(alist) - 1
	while left < right:
		cursum = alist[left] + alist[right]
		if cursum == sumnum:
			return (alist[left],alist[right])
		else:
			if cursum > sumnum:
				right -= 1
			else:
				left += 1
	return False

#和为定值的多个数
'''分析：
若取第n个数，则问题转化为取n-1个数和为sum-n
若不取第你个数，则问题转化为取n-1个数和为sum
'''
list1 = []
def somesum(m,n):
	if (n<=0 or m<=0):
		return

	if m == n:
		print(list1,"+",n)

	list1.append(n)
	somesum(m-n,n-1)
	list1.pop()
	somesum(m,n-1)


