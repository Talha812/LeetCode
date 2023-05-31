class Solution:
    def customSortString(self, order: str, s: str) -> str:
        dic = {}
        for i in range(len(order)):
            dic[order[i]] = i
        
        alph = "abcdefghijklmnopqrstuvwxyz"
        for ch in alph:
            if ch not in dic:
                dic[ch] = 27
        
        splt_s = []
        for ch in s:
            splt_s.append(ch)
        
        for step in range(1, len(s)):
            key = splt_s[step]
            j = step - 1
                            
            while j >= 0 and dic[key] < dic[splt_s[j]]:
                splt_s[j + 1] = splt_s[j]
                j = j - 1

            splt_s[j + 1] = key
        
        return "".join(splt_s)