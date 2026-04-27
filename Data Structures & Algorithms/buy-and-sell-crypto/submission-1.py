class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        smallest = prices[0]
        for i in prices:
            difference = i - smallest
            if i <= smallest:
                smallest = i
            if difference > profit:
                profit = difference
            
           
        
        return profit

