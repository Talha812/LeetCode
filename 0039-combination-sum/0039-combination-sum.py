class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        global ans
        ans = []
        def calculateSum(candidates, path, target):
            global ans
            if target < 0:
                return
            
            if target == 0:
                ans.append(path[:])
                return
            
            for i in range(len(candidates)):
                calculateSum(candidates[i:], path + [candidates[i]], target - candidates[i])
        
        calculateSum(candidates, [], target)
        return ans