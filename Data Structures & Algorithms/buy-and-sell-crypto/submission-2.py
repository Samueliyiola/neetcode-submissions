class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        smallest = prices[0]
        for i in prices:

            if i <= smallest:
                smallest = i
            profit = max(profit, i - smallest)
            
           
        
        return profit

