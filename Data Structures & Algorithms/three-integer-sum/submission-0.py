class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        result = []

        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            
            while j < k:
                individual_result = []
                if nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                elif nums[i] + nums[j] + nums[k] == 0:
                    individual_result.append(nums[i])
                    individual_result.append(nums[j])
                    individual_result.append(nums[k])
                    if individual_result not in result:
                        result.append(individual_result)
                    j += 1
                    k -= 1               

        return result


            
        