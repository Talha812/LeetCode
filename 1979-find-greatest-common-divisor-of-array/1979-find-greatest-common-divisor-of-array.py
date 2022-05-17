class Solution:
    def findGCD(self, nums: List[int]) -> int:
        
        max_num = max(nums)
        min_num = min(nums)
        
        greatestDivisor = 1
        for divisor in range(2,min_num+1):
            if(min_num%divisor == 0 and max_num%divisor == 0):
                greatestDivisor = divisor
        
        return greatestDivisor
    