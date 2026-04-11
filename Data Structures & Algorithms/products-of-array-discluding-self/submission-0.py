class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        i = 0
        result = []

        for q in range(len(nums)):
            k = 1
            a = nums.pop(q)

            for j in nums:
                k = int(k * j)   

            result.append(k)
            nums.insert(q, a)
        return result


