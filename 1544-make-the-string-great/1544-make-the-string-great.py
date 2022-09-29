class Solution:
    def makeGood(self, s: str) -> str:
        
        ans = []
        for i in range(len(s)):
            if(i==0):
                ans.append(s[i])
            
            else:
                if(len(ans)>0 and (ord(s[i]) == ord(ans[-1])+32 or ord(s[i]) == ord(ans[-1])-32)):
                    ans.pop()
                else:
                    ans.append(s[i])
                    
        return "".join(ans)
    