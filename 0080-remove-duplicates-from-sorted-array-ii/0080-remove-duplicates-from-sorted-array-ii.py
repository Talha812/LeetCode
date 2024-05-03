class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        # sanity check
        if len(nums) <= 2:
            return len(nums)
        
        placeAt = 2  # Index at which in-place operation will perform 
                     # (This will be last index on which element will be placed)
        i = 2    #  Traverse on the List
        while i < len(nums):
            
            if nums[i] != nums[placeAt - 2]:
                nums[placeAt] = nums[i]
                placeAt += 1
                
            i += 1
            
        return placeAt
        