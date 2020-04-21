class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
            
        profit = 0
        i = 0
        peak = prices[0]
        valley = prices[0]
        while i < len(prices) -1:
            while i < len(prices)-1 and prices[i+1] <= prices[i]:
                i += 1
            valley = prices[i]
            while i < len(prices)-1 and prices[i+1] >= prices[i]:
                i += 1
            peak = prices[i]
            profit = profit +  (peak - valley)

        return profit