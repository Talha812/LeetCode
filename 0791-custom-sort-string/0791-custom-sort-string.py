class Solution:
    def customSortString(self, order: str, s: str) -> str:
        
        
        dic = {}
        
        for ch in s:
            if ch in dic:
                dic[ch] += 1
            else:
                dic[ch] = 1
        
        
        ans = ""
        
        for ch in order:
            if ch in dic:
                ans += (ch*dic[ch])
                del dic[ch]
        
        if dic:
            for ch, v in dic.items():
                ans += ch*v
        
        return ans