class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices == []:
            return 0
        min_price = prices[0]
        profit = 0
        for i in prices:
            if i < min_price:
                min_price = i
            elif i - min_price > profit:
                profit = i - min_price
        return profit
                
# Runtime: 72 ms, faster than 78.94% of Python3 online submissions for Best Time to Buy and Sell Stock.
# Memory Usage: 14.7 MB, less than 5.75% of Python3 online submissions for Best Time to Buy and Sell Stock.
