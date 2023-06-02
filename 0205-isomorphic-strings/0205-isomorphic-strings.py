class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        dicS_T = {}
        dicT_S = {}
        for i in range(len(s)):
            if(s[i] not in dicS_T and t[i] not in dicT_S):
                dicS_T[s[i]] = t[i]
                dicT_S[t[i]] = s[i]
                
            elif(dicS_T.get(s[i]) != t[i] or dicT_S.get(t[i]) != s[i]):
                return False

        return True