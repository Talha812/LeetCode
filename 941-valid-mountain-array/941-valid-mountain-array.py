class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        if(len(arr) >= 3):
            
            maximum = max(arr)
            max_ind = arr.index(maximum)
            
            if(max_ind == len(arr)-1 or max_ind == 0):
                return False
            
            # Checking before maxmimum height
            for i in range(max_ind):
                if(arr[i] >= arr[i+1]):
                    return False
                else:
                    continue
                    
            # Checking after maximum height
            for i in range(max_ind, len(arr)-1):
                if(arr[i+1]>= arr[i]):
                    return False
                else:
                    continue
                
            return True
        
        return False