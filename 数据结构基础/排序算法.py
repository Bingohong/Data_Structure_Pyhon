# 排序算法
#-------------------------------选择排序-----------------------------
def findSmallest(arr):
	smallest = arr[0]
	smallest_index = 0
	for i in range(1,len(arr)):
		if arr[i] < smallest:
			smallest = arr[i]
			smallest_index = i
	return smallest_index

def selectionSort(arr):
	newArr = []
	for i in range(len(arr)):
		smallest = findSmallest(arr)
		newArr.append(arr.pop(smallest))
	return newArr

def selectionSort(arr):
	for fillslot in range(len(arr)-1,0,-1):
		positionmax = 0
		for location in range(1,fillslot+1):
			if arr[location] > arr[positionmax]:
				positionmax = location
		temp = arr[fillslot]
		arr[fillslot] = arr[positionmax]
		arr[positionmax] = temp

#-------------------------------快速排序-----------------------------
def quickSort(array):
	if len(array) < 2:
		return array
	else:
		pivot = array[0]
		less = [i for i in array[1:] if i <= pivot]
		more = [i for i in array[1:] if i > pivot]
		return quickSort(less) + [pivot] + quickSort(more)

#------------------------------冒泡排序------------------------------
def bubbleSort(array):
	for passnum in range(len(array)-1,0,-1):
		for i in range(passnum):
			if array[i] > array[i+1]:
				array[i],array[i+1] = array[i+1],array[i]
	return array		

#----------------------------短路冒泡排序------------------------------
def shortBubbleSort(array):
	exchanges = True
	passnum = len(array) - 1
	while passnum > 0 and exchanges:
		exchanges = False 
		for i in range(passnum):
			if array[i] > array[i+1]:
				array[i], array[i+1] = array[i+1], array[i]
				exchanges = True
		passnum -= 1
	return array

#--------------------------插入排序---------------------------------
def insertSort(array):
	for index in range(1,len(array)):
		currentValue = array[index]
		position = index
		while position > 0 and array[position-1] > currentValue:
			array[position] = array[position-1]
			position -= 1
		array[position] = currentValue
	return array

# -----------------------希尔排序(缩小间隔排序)-----------------------
def shellSort(array):
	sublistcount = len(array) // 2
	while sublistcount > 0:
		for startposition in range(sublistcount):
			gapInsertSort(array,startposition,sublistcount)
		sublistcount //= 2

def gapInsertSort(array, start, gap):
	for i in range(start+gap, len(array), gap):
		currentValue = array[i]
		position = i
		while position >= gap and array[position-gap] > currentValue:
			array[position] = array[position-gap]
			position -= gap
		array[position] = currentValue

#-----------------------归并排序------------------------------
 def mergeSort(array):
 	print("spliting: ",array)
 	if len(array) > 1:
 		mid = len(array) // 2
 		lefthalf = array[:mid]
 		righthalf = array[mid:]

 		mergeSort(lefthalf)
 		mergeSort(righthalf)

 		i=j=k=0

 		while i < len(lefthalf) and j < len(righthalf):
 			if lefthalf[i] < righthalf[j]:
				array[k]=lefthalf[i]
				i=i+1
			else:
				array[k]=righthalf[j]
				j=j+1
			k=k+1

		while i < len(lefthalf):
			alist[k]=lefthalf[i]
			i=i+1
			k=k+1

		while j < len(righthalf):
			alist[k]=righthalf[j]
			j=j+1
			k=k+1
	print("Merging: ",alist)




