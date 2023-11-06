class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        
        dic = {}
        
        for d in dominoes:
            if (d[0], d[1]) in dic:
                dic[(d[0], d[1])] += 1
                
            elif (d[1], d[0]) in dic:
                dic[(d[1], d[0])] += 1
                
            else:
                dic[(d[0], d[1])] = 1
        
        def calculate(n):
            
            q = 1
            r = 1
            
            for i in range(1, n+1):
                q *= i
            
            for i in range(1, n-1):
                r *= i
            
            r *= 2
            
            return q//r
        
        ans = 0
        for k, v in dic.items():
            if v > 1:
                ans += calculate(v)
        
        return ans