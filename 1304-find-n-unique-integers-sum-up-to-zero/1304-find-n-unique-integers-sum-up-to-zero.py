class Solution:
    def sumZero(self, n: int) -> List[int]:
        
        ans = []
        if n%2 == 0:
            for n in range(1, (n//2)+1):
                ans.append(n)
                ans.append(-1*n)
        else:
            for n in range(0, (n//2)+1):
                if n == 0:
                    ans.append(n)
                else:
                    ans.append(n)
                    ans.append(-1*n)

        return ans