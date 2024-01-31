class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        nums.sort()
        
        while len(nums) > 2 and nums[-1] >= nums[-2] + nums[-3]:
            nums.pop()
            
        return 0 if len(nums) < 3 else sum(nums[-3:])