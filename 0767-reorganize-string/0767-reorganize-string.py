class Solution:
    def reorganizeString(self, s: str) -> str:
        
        dic = {}
        for i in s:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        
        ch_cnt = []
        
        for k, val in dic.items():
            ch_cnt.append((val, k))
        
        ch_cnt.sort()
        
        
        ans = [0] * len(s)
        if ch_cnt[-1][0] > (len(s)+1)//2:
            return ""
        
        i = 0
        while ch_cnt:
            cnt, ch = ch_cnt.pop()
            
            while cnt != 0:
                ans[i] = ch
                cnt -= 1
                i += 2
                if i >= len(s):
                    i = 1
        
        return "".join(ans)
                
            
        
        
        