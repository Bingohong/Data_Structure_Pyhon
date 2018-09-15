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

# 高位优先排序法
'''逻辑解释：
1).http://www.dayexie.com/detail639261.html
2).https://www.tuhd.top/2017/06/27/2017-06-27-5%E5%AD%97%E7%AC%A6%E4%B8%B25-1%E5%AD%97%E7%AC%A6%E4%B8%B2%E6%8E%92%E5%BA%8F/
3).https://www.tuhd.top/2017/06/27/2017-06-27-5%E5%AD%97%E7%AC%A6%E4%B8%B25-1%E5%AD%97%E7%AC%A6%E4%B8%B2%E6%8E%92%E5%BA%8F/
'''
# 选用一个R=26的字母表，涵盖小写字母
R = 26
def charAt(s, d):
    if d==len(s):
        return -1
    else:
        return ord(s[d])-ord("a")

# 将字符串数组从[io,hi]的元素s[i]按照第d个字母排序
def sort(s, lo, hi, d, aux):
    if hi<=lo:
        return
    
    count = [0] * (R+2)
    
    # 计算频数
    for i in range(lo,hi+1):
        c = charAt(s[i], d)
        count[c+2] += 1
        
    # 频数转换为索引
    for r in range(0,R+1):
        count[r+1] += count[r]
        
    # 数据分类
    for i in range(lo,hi+1):
        c = charAt(s[i],d)
        aux[count[c+1]] = s[i]
        count[c+1] += 1
        
    # 回写
    for i in range(lo,hi+1):
        s[i] = aux[i-lo]
    
    # 递归排序
    for r in range(0,R):
        sort(s, lo+count[r], lo+count[r+1]-1, d+1, aux)
        
# 输入
s = ["she",
     "sells",
     "seashells",
     "by",
     "the",
     "sea",
     "shore",
     "the",
     "shells",
     "she",
     "sells",
     "are",
     "surely",
     "seashells"]

n = len(s)
aux = ["0"]*n
sort(s,0,n-1,0,aux)

# 结果
res= ['are',
     'by',
     'sea',
     'seashells',
     'seashells',
     'sells',
     'sells',
     'she',
     'she',
     'shells',
     'shore',
     'surely',
     'the',
     'the']
