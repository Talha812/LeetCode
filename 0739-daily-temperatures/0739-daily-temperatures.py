class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        n = len(temperatures)
        stack = []
        ans = [0] * n
        for i in range(n-1, -1, -1):
            if i == n-1:
                ans[i] = 0
            
            while stack and stack[-1][0] <= temperatures[i]:
                stack.pop()
            
            if stack:
                ans[i] = stack[-1][1]-i
            
            stack.append([temperatures[i], i])
        
        return ans