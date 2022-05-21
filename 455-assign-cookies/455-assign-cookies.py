class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        count = 0
        g.sort()
        s.sort()
        
        for i in g:
            for j in range(len(s)):
                if(i <= s[j]):
                    s.pop(j)
                    count += 1
                    break
        
        return count