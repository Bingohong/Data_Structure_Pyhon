''' 招商银行信用卡中心2018秋招编程题
 * 小招喵跑步
 * 小招喵喜欢在数轴上跑来跑去，假设它现在站在点n处，它只会3种走法，分别是：
 * 1.数轴上向前走一步，即n=n+1
 * 2.数轴上向后走一步,即n=n-1
 * 3.数轴上使劲跳跃到当前点的两倍，即n=2*n
 * 现在小招喵在原点，即n=0，它想去点x处，快帮小招喵算算最快的走法需要多少步？
 * 输入描述:
 * 小招喵想去的位置x
 * 输出描述:
 * 小招喵最少需要的步数
 * 输入例子1:
 * 3
 * 输出例子1:
 * 3
'''
'''解题思路：
从x倒着回到0
偶数，能跳的就跳，即n//2+1,加1是因为跳了一步
奇数，向前或前后走一步，变为偶数，能跳就跳，(n+1)//2+2，加2是因为走了一步又跳了一步
'''
def count(n):
    if n<0:
        n = -n
    if n==0:
        print("select n=0")
        return 0
    elif n==1:
        print("select n=1")
        return 1
    if n%2==0:
        print("select jumpping")
        return count(n//2)+1
    else:
        print("select moving_1_step")
        r1 = count((n+1)//2) + 2
        print("r1 ",r1)
        r2 = count((n-1)//2) + 2
        print("r2 ",r2)
        return min(r1, r2)

'''测试用例：count(3)
select moving_1_step
select jumpping
select n=1
r1  4
select n=1
r2  3
'''