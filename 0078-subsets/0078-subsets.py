class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        global ans
        ans = []
        
        def dfs(nums, start, path):
            global ans
            
            if len(path) >= 0:
                ans.append(path[:])
            
            for i in range(start, len(nums)):
                path.append(nums[i])
                dfs(nums, i+1, path)
                path.pop()
            
        
        dfs(nums, 0, [])
        
        return ans
        