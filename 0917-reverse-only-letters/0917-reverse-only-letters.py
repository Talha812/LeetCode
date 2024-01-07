class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        
        ans = []
        j = len(ans)-1
        for i in range(len(s)):
            if s[i].isalpha():
                while not s[j].isalpha():
                    j -= 1
                    
                ans.append(s[j])
                j -= 1
            else:
                ans.append(s[i])
                
        return "".join(ans)