class Solution:
    def findGCD(self, nums: List[int]) -> int:
        
        max_num = max(nums)
        min_num = min(nums)
        
        ans = 1
        for i in range(2,min_num+1):
            if(min_num%i == 0 and max_num%i == 0):
                ans = i
        
        return ans
    