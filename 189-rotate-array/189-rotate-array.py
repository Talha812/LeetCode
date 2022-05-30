class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        if len(nums) == k or k == 0 or len(nums) == 1:
            pass
        else:
            for i in range(k):
                nums.insert(0, nums.pop())
#             for i in range(k):
#                 temp = nums[-1]
#                 for j in range(len(nums)-2, -1, -1):
#                     nums[j+1] = nums[j]
                
#                 nums[0] = temp
            
#             #print(nums)