# 题目见https://leetcode-cn.com/problems/circular-array-loop/description/
# 解法如下：
def circularArrayLoop(nums):
    '''判断是否存在环，可用快慢指针
    '''
    n = len(nums)
    for i in range(n):
        if nums[i]==0:
            continue
        print("i",i)
        slow = i
        fast = getNextIndex(nums, slow)
        # 方向相同时才会继续遍历
        # 判断方向时仅需要fast指针就可以，因为slow一定包含在fast过程
        while (nums[i]*nums[fast]>0) & (nums[i]*nums[getNextIndex(nums,fast)]>0):
            print(slow, fast)
            if slow==fast: # 快慢指针指向相同位置时，才有可能存在环
                if slow==getNextIndex(nums,slow):# 判断slow跳跃前后的指向位置是否相同
                    break # 若相同则不是环
                return True
            slow = getNextIndex(nums,slow) # 慢指针移动一次
            fast = getNextIndex(nums, getNextIndex(nums, fast)) # 快指针移动两次
        
    return False
        
def getNextIndex(nums, ind):
    # python与C两种方式的取余数操作
    # python属于floored-division，结果符号与除数相同
    # C属于truncated-division,结果符号与被除数相同
    fun = lambda x,n:x-n*int(x/n)
    n = len(nums)
    nextInd = ind + nums[ind]
    # nextInd为负数时，需要“取余数+列表长度”处理
    nextInd = fun(nextInd, n) if nextInd>=0 else (fun(nextInd,n) + n)
#     print(ind, nextInd)
    return nextInd
