class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pro = 0
        for i in range(len(prices)):
            buyprice = prices[i]
            for j in range(i+1,len(prices)):
                sellprice = prices[j]
                pro = max(pro, sellprice - buyprice)
        return pro
