class Solution:
    def findMin(self, nums: List[int]) -> int:
        a = nums[0]
        minimum = nums[0]
        for i in range(len(nums)):
            if nums[i] >= a:
                a = nums[i]
            else:
                a = nums[i]
                return a
        
        return minimum


