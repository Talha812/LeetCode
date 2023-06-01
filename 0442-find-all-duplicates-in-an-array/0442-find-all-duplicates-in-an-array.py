class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        i = 0
        while i<len(nums):
            correctInd = nums[i]-1
            if nums[i] != nums[correctInd]:
                nums[i], nums[correctInd] = nums[correctInd], nums[i]
            else:
                i += 1
        

        ans = []
        for i in range(len(nums)):
            if nums[i] != i+1:
                ans.append(nums[i])
        
        return ans