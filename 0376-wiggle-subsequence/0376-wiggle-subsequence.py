class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        
        small_large = 1
        large_small = 1
        for i in range(1, len(nums)):
            if nums[i]>nums[i-1]:
                small_large = large_small + 1
                
            elif nums[i] < nums[i-1]:
                large_small = small_large + 1
                
        res = max(small_large, large_small)
        return res
    