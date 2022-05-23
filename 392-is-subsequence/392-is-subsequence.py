class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        def findIndex(self, t, ch, start, end):
            for i in range(start, end):
                if t[i] == ch:
                    return i
            return -1
        
        s = "z" + s
        record = [-1]
        for i in range(1,len(s)):
            if s[i] in t:
                ind = findIndex(self, t, s[i], record[-1]+1, len(t))
                if(ind > record[-1]):
                    record.append(ind)
                else:
                    return False
            else:
                if(i!=0):
                    return False
        return True
                
                