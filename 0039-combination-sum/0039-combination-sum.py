class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ans = []
        
        def calculate(candidates, path, target):
            if target < 0:
                return
            
            if target == 0:
                ans.append(path)
            
            for i in range(len(candidates)):
                calculate(candidates[i:], path + [candidates[i]], target - candidates[i])
            
        
        calculate(candidates, [], target)
        return ans