class Solution:
    def customSortString(self, order: str, s: str) -> str:
        
        dic = {"" : 27}
        for i in range(len(order)):
            dic[order[i]] = i
        
        alph = "abcdefghijklmnopqrstuvwxyz"
        for ch in alph:
            if ch not in dic:
                dic[ch] = 27
        
        splt_s = []
        for ch in s:
            splt_s.append(ch)
        
        extra = ""
        
        for step in range(1, len(s)):
            key = splt_s[step]
            j = step - 1
            
            # if key not in dic:
            #     extra += splt_s[step]
            #     splt_s[step] = ""
            #     continue
                
            while j >= 0 and dic[key] < dic[splt_s[j]]:
                splt_s[j + 1] = splt_s[j]
                j = j - 1

            splt_s[j + 1] = key
        
        return "".join(splt_s) + extra