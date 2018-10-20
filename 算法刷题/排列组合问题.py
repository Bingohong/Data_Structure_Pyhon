#---------------------------全排列/全组合问题--------------------
#全排列问题
#无重复字符串排列问题---递归方法
'''分析：
将第一个元素与后面元素依次交换，再将除第一个元素外的所有元素递归
abc -> abc ->递归bc 
abc -> bac ->递归ac
abc -> cba ->递归ba
'''
def permutation(pstring,start,length):
	if start == length - 1:
		print(pstring)
	else:
		for i in range(start,length):
			pstring = swap(pstring,start,i)
			permutation(pstring,start+1,length)
			pstring = swap(pstring,start,i)
			

def swap(pstring,start,end):
	p = list(pstring)
	p[start],p[end] = p[end],p[start]
	pstring = "".join(p)
	return pstring

#有重复字符串排列问题
'''分析：
去重全排列就是第一个字符仅与出现过一次的字符交换
第i个数与第j个数交换时，要求[i,j)中没有与第j个数相等的数
abbb -> babb ->递归abb 
bbab不交换，因为第1个字符a与第3个字符b的区间[1,3)中重复出现了字符b
同理不交换bbba
'''
def isswap(pstring,start,end):
	for i in range(start,end):
		if pstring[i] == pstring[end]:
			return False
	return True

def permutation(pstring,start,length):
	if start == length - 1:
		print(pstring)
	else:
		for i in range(start,length):
			if isswap(pstring,start,i):
				pstring = swap(pstring,start,i)
				permutation(pstring,start+1,length)
				pstring = swap(pstring,start,i)

#全组合问题
#位图法
'''分析：
假设原有元素n个,则最终组合结果是2^n−1个。
采用位操作方法：假设元素原本有：a,b,c，则1表示取该元素，0表示不取。
则001/111分别代表a/abc
'''
def combination(pstring):
	n = len(pstring)
	cnum = 1<<n
	for i in range(1,cnum):#遍历1～2^n-1次
		s = []
		for j in range(n):
			if (i & (1<<j)):#对应位为1时，输出该字符
				s.append(pstring[j])
		print("".join(s))
		del s

# 给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def getcombine(res, temp, start, num, n, k):
            if num==k:
                res.append(temp[:]) #做一次拷贝
                return 
            else:
                for i in range(start,n):
                    temp.append(i)
                    getcombine(res, temp, i+1, num+1, n, k)
                    temp.pop()
                    
        res = []
        temp = []
        getcombine(res, temp, 1, 0, n+1, k)
        return res

		
