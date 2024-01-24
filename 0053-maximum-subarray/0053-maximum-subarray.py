class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        if not nums:
            return 0

        n = len(nums)
        memo = [0] * n

        memo[0] = nums[0]
        max_sum = nums[0]

        for i in range(1, n):
            memo[i] = max(nums[i], memo[i - 1] + nums[i])
            max_sum = max(max_sum, memo[i])

        return max_sum