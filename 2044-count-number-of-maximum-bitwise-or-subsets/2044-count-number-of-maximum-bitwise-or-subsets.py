class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        
        def calculateOR(elements):
            ans = 0
            for n in elements:
                ans = ans|n
            
            return ans
        
        dic = {}
        
        def dfs(nums, start, path):            
            if len(path) > 0:
                output = calculateOR(path)
                if output in dic:
                    dic[output] += 1
                else:
                    dic[output] = 1
                    
            for i in range(start, len(nums)):
                path.append(nums[i])
                dfs(nums, i+1, path)
                path.pop()
        
        dfs(nums, 0, [])
        
        
        maxOR = max(dic.keys())
        
        for k, v in dic.items():
            if k == maxOR:
                return v
        
        