'''统计数组中的逆序对
数组中两个数字，如果前一个数字大于后面的数字，则组成一对逆序对。
解法：类似于归并排序，归并过程计数，最终数组为递增序列。
两种代码：1）由剑指offer的C++代码迁移过来 2）由python版本的归并排序代码修改过来
'''
# -----------------------------------1）由剑指offer的C++代码迁移过来--------------------------------------
def inversePairs(alist, cplist, start, end):
    if start==end:
        cplist[start] = alist[start]
        return 0
    
    length = (end-start)//2
    print("left arr: ", alist[start:start+length+1])
    print("right arr: ", alist[start+length+1:end+1])
    left = inversePairs(cplist, alist, start, start+length)
    right = inversePairs(cplist, alist, start+length+1, end)
    print("left ", left, "right ",right)
    print("start ",start, "end ", end, "length ",length)

    i = start+length # 指向前一段的最后位置
    j = end # 指向后一段的最后位置
    cpind = end
    count = 0
    
    # 注意i，j循环条件为start\start+length+1
    while i>=start and j>=start+length+1:
        if alist[i]> alist[j]:
            cplist[cpind] = alist[i]
            count += j - start - length
            cpind -= 1
            i -= 1
        else:
            cplist[cpind] = alist[j]
            cpind -= 1
            j -= 1
    
    while i>=start:
        cplist[cpind] = alist[i]
        cpind -= 1
        i -= 1
    
    while j>=start+length+1:
        cplist[cpind] = alist[j]
        cpind -= 1
        j -= 1
    print("cplist left arr: ", cplist[start:start+length+1])
    print("cplist right arr: ", cplist[start+length+1:end+1])
    print("count ", count)
    print("-----round end------------")
    return count + left + right
    
def inverse(alist):
    n = len(alist)
#     cplist = [0] * n
    cplist = alist.copy()
    print(cplist)
    res = inversePairs(alist, cplist, 0, n-1)
    print(cplist)
    return res
    
'''result
alist = [7,5,6,4,2] // 9
[7, 5, 6, 4, 2]
left arr:  [7, 5, 6]
right arr:  [4, 2]
left arr:  [7, 5]
right arr:  [6]
left arr:  [7]
right arr:  [5]
left  0 right  0
start  0 end  1 length  0
cplist left arr:  [5]
cplist right arr:  [7]
count  1
-----round end------------
left  1 right  0
start  0 end  2 length  1
cplist left arr:  [5, 6]
cplist right arr:  [7]
count  1
-----round end------------
left arr:  [4]
right arr:  [2]
left  0 right  0
start  3 end  4 length  0
cplist left arr:  [2]
cplist right arr:  [4]
count  1
-----round end------------
left  2 right  1
start  0 end  4 length  2
cplist left arr:  [2, 4, 5]
cplist right arr:  [6, 7]
count  6
-----round end------------
[2, 4, 5, 6, 7]
'''

# -----------------------------------------2）由python版本的归并排序代码修改过来--------------------------------------------
def mergeSort(alist):
    print("splitting: ", alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        
        left = mergeSort(lefthalf)
        right = mergeSort(righthalf)
        
        i = len(lefthalf) - 1 $ 指向左边最后位置
        j = len(righthalf) - 1 # 指向右边最后位置
        ind = j + i + 1 # 指向原数组最后位置
        count = 0
        
        # 注意循环条件为>0
        while i>=0 and j>=0:
            if lefthalf[i]>righthalf[j]:
                alist[ind] = lefthalf[i]
                ind -= 1
                i -= 1
                count += j + 1
            else:
                alist[ind] = righthalf[j]
                ind -= 1
                j -= 1
                
        while i>=0:
            alist[ind] = lefthalf[i]
            ind -= 1
            i -= 1
        
        while j>=0:
            alist[ind] = righthalf[j]
            ind -= 1
            j -= 1
        print("left ",left, "right ",right, "count ", count)
        return count + left + right
    else:
        return 0
    print(alist)
'''result
alist = [7,5,6,4,2] // 9
splitting:  [7, 5, 6, 4, 2]
splitting:  [7, 5]
splitting:  [7]
splitting:  [5]
left  0 right  0 count  1
splitting:  [6, 4, 2]
splitting:  [6]
splitting:  [4, 2]
splitting:  [4]
splitting:  [2]
left  0 right  0 count  1
left  0 right  1 count  2
left  1 right  3 count  5
'''
