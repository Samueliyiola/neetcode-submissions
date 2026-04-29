class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        arr = sorted(list(s1))
        size = len(s1)
        left = 0
        right = size 
        while right <= len(s2):
            if (arr == sorted(list(s2[left:right]))):
                return True
            left += 1
            right += 1
        
        return False
            

