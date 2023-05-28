class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        def calculate(nums, path):
            
            if len(nums) == 0:
                ans.append(path)
                return

            for i in range(len(nums)):
                calculate(nums[:i] + nums[i+1:], path + [nums[i]])
                            
        
        calculate(nums, [])
        return ans