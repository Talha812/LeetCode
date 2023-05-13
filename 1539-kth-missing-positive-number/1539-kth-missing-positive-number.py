class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        output = 1
        i = 0
        count = 0
        while True:
            if (i<len(arr) and arr[i] != output) or i >= len(arr):
                count += 1
                if count == k:
                    return output
            else:
                i += 1
                
            output += 1
            
        return output
            