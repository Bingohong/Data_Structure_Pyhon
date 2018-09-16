"""问题：股票交易最大收益
在股市的交易日中，假设最多可进行两次买卖(即买和卖的次数均小于等于2)，
规则是必须一笔成交后进行另一笔(即买-卖-买-卖的顺序进行)。
给出一天中的股票变化序列，请写一个程序计算一天可以获得的最大收益。
请采用实践复杂度低的方法实现。

给定价格序列prices及它的长度n，请返回最大收益。保证长度小于等于500。

测试样例：
[10,22,5,75,65,80],6
返回：87
"""
# 解法1,dp动态规划，以第i天为界，划分两个区间，计算最大收益
def maxProfitdp(prices,n):
    pre_profit = [0]*n
    post_profit = [0]*n
    
    # 第i天之前进行第一次交易获得的最大利润
    min_buy = prices[0]
    for i in range(1,n):
        min_buy = min(prices[i],min_buy)
        pre_profit[i] = max(pre_profit[i-1], prices[i]-min_buy)
    
    # 第i天之后进行第二次交易获得的最大利润
    max_sell = prices[-1]
    for j in range(n-2,-1,-1):
        max_sell = max(prices[j],max_sell)
        post_profit[j] = max(post_profit[j+1], max_sell-prices[j])
    
    # 将两次利润相加，得到的最大利润为最终最大利润
    max_profit = 0
    for k in range(0,n):
        max_profit = max(max_profit, pre_profit[k]+post_profit[k])
        print(max_profit)
    print("pre_profit: ",pre_profit)
    print("post_profit: ", post_profit)
    return max_profit

# 解法2，剩余的钱越多越好
def maxProfit(prices,n):
    # 初始认为买入会花费无穷大值
    buy1, buy2, buy3 = -99999999, -99999999, -99999999
    # 初始认为卖出收获为0
    sale1, sale2, sale3 = 0.0, 0.0, 0.0
    # 遍历每个价格，认为手中剩余钱越多越赞！
    # 买入时手中钱会减少，卖出会增加。每次手中的资本都是在前次操作基础累加
    for x in prices:
        print(x)
        buy1 = max(buy1, -x)        # 第一次买入
        sale1 = max(sale1, buy1+x)  # 第一次卖出
        buy2 = max(buy2, sale1-x)   # 第二次买入
        sale2 = max(sale2, buy2+x)  # 第二次卖出
        buy3 = max(buy3, sale2-x)   # 第三次买入
        sale3 = max(sale3, buy3+x)  # 第三次卖出
    
        print("buy1 %d,  buy2 %d, buy3 %d"\
              %(buy1, buy2, buy3))
              
        print("sale1 %d, sale2 %d, sale3 %d"\
              %(sale1, sale2, sale3))
    return sale1, sale2, sale3
"""示例：打印交易3次，每次最大收益
prices = [10,22,5,75,65,80]
n = 6
maxProfit(prices, n)

result:
    10
    buy1 -10,  buy2 -10, buy3 -10
    sale1 0, sale2 0, sale3 0
    22
    buy1 -10,  buy2 -10, buy3 -10
    sale1 12, sale2 12, sale3 12
    5
    buy1 -5,  buy2 7, buy3 7
    sale1 12, sale2 12, sale3 12
    75
    buy1 -5,  buy2 7, buy3 7
    sale1 70, sale2 82, sale3 82
    65
    buy1 -5,  buy2 7, buy3 17
    sale1 70, sale2 82, sale3 82
    80
    buy1 -5,  buy2 7, buy3 17
    sale1 75, sale2 87, sale3 97
    (75, 87, 97)
"""
