class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        
        high = len(s)
        low = 0
        
        ans = []
        
        for i in range(len(s)):
            if(s[i] == "I"):
                ans.append(low)
                low += 1
            elif(s[i] == "D"):
                ans.append(high)
                high -= 1
        
        if(s[-1] == "D"):
            ans.append(high)
        else:
            ans.append(low)
        
        return ans
            