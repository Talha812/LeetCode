class Solution:
    def minOperations(self, s: str) -> int:

        c1 = 0
        flag = 0
        for i in range(len(s)):
            if int(s[i]) != flag:
                c1 += 1
                
            flag = not flag
        
        c2 = len(s) - c1
        
        return min(c1, c2)