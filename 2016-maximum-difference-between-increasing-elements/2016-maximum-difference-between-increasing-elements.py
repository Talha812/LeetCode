class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        
        mini = float("inf")
        maxi = -1
        for i in range(len(nums)):
            mini = min(nums[i], mini)
            maxi = max(nums[i]-mini, maxi)
        
        if maxi == 0:
            return -1
        
        return maxi
            