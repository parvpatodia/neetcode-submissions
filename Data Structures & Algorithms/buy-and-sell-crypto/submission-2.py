class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # pro = 0 
        # for i in range(len(prices)):
        #     buy =  prices[i]
        #     for j in range(i+1,len(prices)):
        #         sell = prices[j]
        #         pro = max(pro,sell-buy)
        # return pro
        l,r = 0,1
        maxPro = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxPro = max(maxPro,profit)
            else:
                l = r
            r += 1
        return maxPro