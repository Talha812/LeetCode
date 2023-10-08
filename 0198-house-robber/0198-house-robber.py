class Solution:
    def rob(self, nums: List[int]) -> int:
        
        curr = 0
        prev = 0
        next = 0
        
        for i in range(len(nums)):
            next = max(prev+nums[i], curr)
            prev = curr
            curr = next
        
        return curr