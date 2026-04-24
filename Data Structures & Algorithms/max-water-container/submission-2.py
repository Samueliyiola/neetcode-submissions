class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        max_cont = 0
        while i < j:
            if heights[i] <= heights[j]:
                product = heights[i] * (j - i)
                i += 1
                
            elif heights[i] > heights[j]:
                product = heights[j] * (j - i)
                j -= 1
            
            if product > max_cont:
                max_cont = product

            
        
        return max_cont

        