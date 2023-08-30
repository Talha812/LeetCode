class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        
        
        def calculate(index, arr):
            if index >= len(arr) or index < 0 or arr[index] < 0:
                return False
            
            if arr[index] == 0:
                return True
            
            arr[index] = -1*arr[index]
            
            return calculate(index+abs(arr[index]), arr) or calculate(index-abs(arr[index]), arr)
        
        return calculate(start, arr)