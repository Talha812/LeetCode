class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        f=0
        s=0
        while f<len(nums):
            if nums[f]!=0:
                if nums[s]==0:
                    nums[s],nums[f]=nums[f],nums[s]
                s+=1
            f+=1