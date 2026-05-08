import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1
        end = max(piles)
        answer = end
        
        while start <= end:
            mid = (start + end) // 2
            minimum = 0
            for i in piles:
                minimum += math.ceil(i / mid)
            if minimum <= h:
                answer = mid
                end = mid - 1
            else:
                start = mid + 1
            
        
        return answer
            

            

