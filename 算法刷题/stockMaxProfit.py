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