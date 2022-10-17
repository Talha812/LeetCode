class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        if(target < nums[0]):
            return 0
        elif(target > nums[len(nums)-1]):
            return len(nums)
        
        start =0
        end = len(nums)-1
        
        while(start<=end):
            mid = (start+end)//2
            if(nums[mid]==target):
                return mid
            elif(nums[mid]>target):
                end = mid-1
            else:
                start = mid+1
        return start