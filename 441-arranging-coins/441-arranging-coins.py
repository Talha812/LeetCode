class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        count = 0
        coins = n
        for i in range(1, n+1):
            if(coins >= i):
                count += 1
                coins -= i
            else:
                break
        
        return count