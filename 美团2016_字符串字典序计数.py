'''美团2016_字符串字典序计数
求字典序在s1和s2之间的，长度在len1到len2的字符串的个数，结果mod 1000007。

输入描述:
每组数据包涵s1（长度小于100），s2（长度小于100），len1（小于100000），len2（大于len1，小于100000）

输出描述:
输出答案。

输入例子1:
ab ce 1 2

输出例子1:
56
'''
'''解题思路：
首先要搞清楚字典序的意思：即从两个字符串的下标为0开始进行对比，字典序是从左往右进行对比的。 
例如ab，abc这样两者之间的字符串个数为aba、abb，
而ab、bb两者之间的字符串个数为：ac、ad、ae…az、ba这26个，
所以高位的字符串个数要是26的i次幂。 
其次，要理解题目的“长度在len1到len2的字符串的个数”，
指的是长度在len1的字符串个数、长度在len1+1的字符串个数、长度为len2的字符串个数。 
例abcde、acede这两个字符串，长度为1到4表示的是长度为1的时候两个字符a、a之间的个数，
长度为2的时候两个字符ab、ac之间的个数，长度为3的时候abc、ace两个字符串之间的个数，长度为4：abcd、aced的个数。 
所以计算的时候应该以长度作为变量遍历len1到len2之间的字符串个数，最后相加。
'''
# 字典序计数 只包含小写字母类似于26进制计算
def lexicalNums(s1, s2, len1, len2):
	# 将s1和s2补长到len2长度
    s1 = s1+"a"*(len2-len(s1))
    s2 = s2+"z"*(len2-len(s2))
    print(s1,"\n",s2)
    # arr数组记录每个位置的差
    arr = [0]*len2
    for i in range(len2):
        arr[i] = ord(s2[i])-ord(s1[i])
    print(arr)
    # 依次从len1->len2遍历计算数目
    cnums = 0
    for i in range(len1, len2+1):
        temp = 0
        for j in range(i):
            temp = temp*26 + arr[j]
        print(i, temp)
        cnums += temp
    # 所有字符串不包含s2自身，最后要减1
    return cnums-1

# ------------------------------------------------------------------------------------
'''类似题目：字典序排数(leetCode)
给定一个整数 n, 返回从 1 到 n 的字典顺序。
例如，
给定 n =1 3，返回 [1,10,11,12,13,2,3,4,5,6,7,8,9] 。
'''
def lexicalOrder(n):
    """
    :type n: int
    :rtype: List[int]
    """
    '''字典序的更新顺序
    curr*10 先增加长度
    curr+1  再增加数值
    curr//10 + 1 末位到9时，要降位
    '''
    arr = []
    curr = 1
    for i in range(1,n+1):
        arr.append(curr)
        if curr*10<=n:
            curr *= 10
        elif curr%10!=9 and curr+1<=n:
            curr += 1
        else:
            curr //= 10
            while (curr)%10==9:
                curr //= 10
            curr = curr + 1
    return arr