class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        j = 1
        length = len(prices) - 1
        for i in range(len(prices)):
            j = i + 1
            while j <= length:
                difference = prices[j] - prices[i]
                if difference > profit:
                    profit = difference
                j += 1
        
        return profit


        