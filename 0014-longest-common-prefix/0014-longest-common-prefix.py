class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        str1 = min(strs)
        str2 = max(strs)

        i=0
        while(i<len(str1)):
            if(str1[i] != str2[i]):
                str1 = str1[:i]
                break
            i+=1
        
        return str1
        