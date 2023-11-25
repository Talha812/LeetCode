class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        
        arr.sort()
        
        diff = abs(arr[0] - arr[1])
        
        for i in range(1, len(arr)):
            if diff != abs(arr[i]-arr[i-1]):
                return False
        
        return True