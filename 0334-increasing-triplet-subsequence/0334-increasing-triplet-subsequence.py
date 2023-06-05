class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        if len(nums) < 3:
            return False

        left = float('inf')
        mid = float('inf')
        
        for n in nums:
            right = n
            
            if right > mid:
                return True
            
            if right < mid and right > left:
                mid = right
                
            elif right < left:
                left = right
        
        return False