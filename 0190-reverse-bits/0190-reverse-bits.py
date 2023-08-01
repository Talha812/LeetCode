class Solution:
    def reverseBits(self, n: int) -> int:

        ans = 0
        power = 31
        
        while n > 0:
            rem = n%2
            ans = ans + (int(rem)*pow(2,power))
            n = n//2
            power -= 1
        
        return ans