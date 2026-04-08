class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        distinct = set(nums)
        if(len(distinct) < len(nums)):
            return True
        else:
            return False
        