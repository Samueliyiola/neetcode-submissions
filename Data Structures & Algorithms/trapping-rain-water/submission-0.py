class Solution:
    def trap(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        leftmax = 0
        rightmax = 0
        area = 0
        while i < j:
            leftmax = max(leftmax, height[i])
            rightmax = max(rightmax, height[j])
            if leftmax < rightmax:
                area += leftmax - height[i]
                i += 1
            else:
                area += rightmax - height[j]
                j -= 1
            
        return area
 





            