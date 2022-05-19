class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for i in range(len(matrix)):
            if(matrix[i][0] <= target and matrix[i][len(matrix[i])-1] >= target):
                left = 0
                right = len(matrix[i])-1
                while(left<=right):
                    mid = (left+right)//2
                    if(matrix[i][mid] == target):
                        return True
                    elif(matrix[i][mid] < target):
                        left = left + 1
                    else:
                        right = right - 1
                
                return False
        
        return False