class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        a = len(matrix)
        b = len(matrix[0]) -1
        for i in range(a):
            if matrix[i][b] > target:
                start = 0
                end = b
                while start <= end:
                    mid = (start + end ) // 2
                    if target == matrix[i][mid]:
                        return True
                    elif target > matrix[i][mid]:
                        start = mid + 1
                    else:
                        end = mid - 1
                
                return False
                    
                    
                    


    
            elif matrix[i][b] == target:
                return True
            
        

        return False


        