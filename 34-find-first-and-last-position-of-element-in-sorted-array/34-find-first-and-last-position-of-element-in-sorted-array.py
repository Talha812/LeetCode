class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        start = 0
        end = len(nums)-1
        
        while(start <= end):
            if(nums[start] < target):
                start += 1
            
            if(nums[end] > target):
                end -= 1
            if(start>len(nums)-1 or end<0):
                break
                
            if(nums[start] == target and nums[end]==target):
                break
        
        if(start>end):
            return [-1,-1]
        else:
            return [start, end]