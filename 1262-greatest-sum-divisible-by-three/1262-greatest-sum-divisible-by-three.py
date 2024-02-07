class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:

        def cal(index, nums, sum, memo):
            if index == len(nums):
                if sum == 0:
                    return 0
                
                return -10000
            
            if (index,(sum+nums[index])%3) in memo:
                return memo[(index,(sum+nums[index])%3)]
            
            option1 = nums[index] + cal(index+1, nums, (sum+nums[index])%3, memo) 
            option2 = cal(index+1, nums, sum, memo)
            
            memo[(index,(sum+nums[index])%3)] = max(option1, option2)
            
            return memo[(index,(sum+nums[index])%3)]
           
        memo = {}
        return cal(0, nums, 0, memo)
