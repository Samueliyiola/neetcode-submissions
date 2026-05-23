class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        unique = {}

        for i in nums:
            if i not in unique:
                unique[i] = 1
            else :
                return i
        