'''问题：美团2017_最大矩形面积
给定一组非负整数组成的数组h，代表一组柱状图的高度，其中每个柱子的宽度都为1。 
在这组柱状图中找到能组成的最大矩形的面积（如图所示）。 
入参h为一个整型数组，代表每个柱子的高度，返回面积的值。
输入描述:
输入包括两行,第一行包含一个整数n(1 ≤ n ≤ 10000)
第二行包括n个整数,表示h数组中的每个值,h_i(1 ≤ h_i ≤ 1,000,000)

输出描述:
输出一个整数,表示最大的矩阵面积。

输入例子1:
6
2 1 5 6 2 3

输出例子1:
10
'''
'''解题思路：
分治法：最大矩形面积只可能有三种情况：
1. 取决于高度最小的柱子，此时面积等于高度乘总长度；
2. 最大面积出现在高度最小的柱子左边；
3. 最大面积出现在高度最小的柱子右边；
'''
def max_ares(height):
    l = len(height)
    idx = height.index(min(height))
    
    v_mid = height[idx] * l
    
    if idx>0:
        v_left = max_area(height[:idx])
    else:
        v_left = 0
        
    if idx<l-1:
        v_right = max_area(height[idx+1:])
    else:
        v_right = 0
        
    return max(v_mid, v_left, v_right)