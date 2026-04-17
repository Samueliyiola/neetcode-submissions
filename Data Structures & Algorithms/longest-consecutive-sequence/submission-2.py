class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        unique = set(nums)
        longest = 0

        for i in unique:
            # j = 0
            if i - 1 in unique:
                continue

            current = i
            length = 1

            while current + 1 in unique:
                current += 1
                length += 1
            
            if length > longest:
                longest = length
            

        return longest


            
            # else:
            #     start.append(i)
        #     # if i + 1 in unique:
        #     #     j += 1
        #     #     i += 1
            
        #     # if j > longest:
        #     #     longest = j
        
        # for i in start:
        #     q = 1
        #     while i + 1 in unique:
        #         q += 1
        #     if q > longest:
        #         longest = q

        # return longest


