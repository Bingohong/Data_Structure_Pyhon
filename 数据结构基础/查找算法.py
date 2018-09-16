#查找算法
#-------------------------顺序查找--------------------------
#无序列表顺序查找
def sequantialSearch(array,item):
	pos = 0
	found = False
	while pos < len(array) and not found:
		if array[pos] == item:
			found = True
		else:
			pos += 1
	return found

#有序列表顺序查找
def orderSequantialSearch(array,item):
	pos = 0
	found = False
	stop = False
	while pos < len(array) and not found and not stop:
		if array[pos] == item:
			found = True
		elif array[pos] > item:
			stop = True
		else:
			pos += 1
	return found

#----------------------二分查找-----------------------
def binarySearch(array,item):
	first = 0
	last = len(array) - 1
	found = False
	while first <= last and not found:
		midpoint = (first + last) // 2
		if array[midpoint] == item:
			found = True
		elif array[midpoint] > item:
			last = midpoint - 1
		else:
			first = midpoint + 1
	return found

#递归版本
def binarySearch(array,item):
	if len(array) == 0:
		return False
	else:
		midpoint = len(array) // 2
		if array[midpoint] == item:
			return True
		elif array[midpoint] > item:
			return binarySearch(array[:midpoint], item)
		else:
			return binarySearch(array[midpoint+1:],item)