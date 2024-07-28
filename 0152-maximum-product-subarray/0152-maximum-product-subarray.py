class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        max_prod = float('-inf')
        
        curr_prod = 1
        
        # forward Pass
        for i in range(len(nums)):
            curr_prod *= nums[i]
            
            max_prod = max(curr_prod, max_prod)
            
            if curr_prod == 0:
                curr_prod = 1
        
        # Backward Pass
        curr_prod = 1
        
        for i in range(len(nums)-1, -1, -1): # start : end : step
            curr_prod *= nums[i]
            
            max_prod = max(curr_prod, max_prod)
            
            if curr_prod == 0:
                curr_prod = 1
        
        return max_prod