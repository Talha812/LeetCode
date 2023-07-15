class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        global ans
        ans = set()
        def dfs(nums, path):
            global ans
            ans.add(tuple(path[:]))
            
            for i in range(len(nums)):
                dfs(nums[i+1: ], path + [nums[i]])
        
        dfs(nums, [])
        
        return list(ans)