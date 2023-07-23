class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        
        
        def calculate(n, target, memo):
            if n == 0 and target == 0:
                return 1
            
            if n == 0 or target < 0:
                return 0
            
            if (n, target) in memo:
                return memo[(n,target)]
            
            possible_ans = 0
            for i in range(1, k+1):
                possible_ans = possible_ans + calculate(n-1, target-i, memo)
            
            memo[(n, target)] = possible_ans
            
            return memo[(n, target)]
        
        memo = {}
        
        return calculate(n, target, memo)%(pow(10,9) + 7)
            