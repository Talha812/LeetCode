class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        
        max_num = max(nums)
        
        for i in nums:
            if(i != max_num and (i/max_num) > 0.5):
                return -1
        
        for i in range(len(nums)):
            if(nums[i] == max_num):
                return i
            
            