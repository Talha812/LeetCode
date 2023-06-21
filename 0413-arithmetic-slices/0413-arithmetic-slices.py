class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        
        if len(nums) < 3:
            return 0
        
        count = 0
        dummy = 0
        for i in range(2, len(nums)):
            if nums[i]-nums[i-1] == nums[i-1]-nums[i-2]:
                dummy += 1
                count += dummy
            else:
                dummy = 0
        
        return count
    

            
            