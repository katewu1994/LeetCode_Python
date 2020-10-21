class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        minprice = prices[0]
        maxprofit = 0
        for i in range(0,len(prices)):
            maxprofit = max(maxprofit,prices[i]- minprice)
            minprice = min(minprice,prices[i])
        return maxprofit