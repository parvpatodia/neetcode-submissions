class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # l, r = 0,1
        # maxpro = 0 
        # while r < len(prices):
        #     if prices[l] < prices[r]:
        #         profit = prices[r] - prices[l]
        #         maxpro = max(maxpro, profit)
        #     else:
        #         l = r 
        #     r+= 1
        # return maxpro
        minBuy = prices[0]
        maxP = 0

        for sell in prices:
            maxP = max(maxP,sell - minBuy)
            minBuy = min(minBuy, sell)
        return maxP
