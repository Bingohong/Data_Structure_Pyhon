# 键索引排序是基础
def indexSort(nums):
    count = [0] * (max(nums)+1)
    print(len(count))
    # 1.统计频数
    for val in nums:
        count[val] += 1
    print(count)
    # 2.频数转化为索引
    for i in range(1,len(count)):
        count[i] += count[i-1]
    print(count)
    # 3.数据分类排序
    aux = [0] * len(nums)
    for val in nums:
        # 起始索引值要-1,每次复制完成后索引要+1,代表下一起个始索引
        aux[count[val-1]] = val
        count[val-1] += 1
    print(aux)
