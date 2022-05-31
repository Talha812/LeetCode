class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        
        array = s.split(" ")
        #print(array)
        
        if(len(array) == k):
            return s
        
        ans = ""
        for i in range(k):
            if(i == k-1):
                ans += array[i]
            else:
                ans += array[i] + " "
        
        return ans