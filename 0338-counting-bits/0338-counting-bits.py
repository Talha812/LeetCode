class Solution:
    def countBits(self, n: int) -> List[int]:
        def countOnes(i):
            
            count = 0
            
            while(i):
                i = i&(i-1)
                count += 1
        
            return count
        ans = []
        for i in range(n+1):
            ans.append(countOnes(i))
        
        return ans
    
    