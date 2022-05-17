class Solution:
    def findGCD(self, nums: List[int]) -> int:
        
        """
        ----> Logic for finding minimum and maximum num
        
        min_num = nums[0]
        for i in range(1,len(nums)):
            if(nums[i] < min_num):
                min_num = nums[i]
        
        max_num = nums[0]
        for i in range(1,len(nums)):
            if(nums[i] > min_num):
                max_num = nums[i]
        
        """
        
        
        max_num = max(nums)
        min_num = min(nums)
        
        greatestDivisor = 1
        for divisor in range(2, min_num+1):
            if(min_num%divisor == 0 and max_num%divisor == 0):
                greatestDivisor = divisor
        
        return greatestDivisor
    