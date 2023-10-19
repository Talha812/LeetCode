class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        
        n = len(nums)
        result = 0
        for i in range(30):
            count = 0
            for num in nums:
                count += (num >> i) & 1
            result += count * (n - count)
        return result
    
#         def calculateDist(x, y):            
#             XOR = x^y
#             dist = 0
#             while XOR > 0:
#                 and_ans = XOR & 1
#                 dist += and_ans
#                 XOR >>= 1
        
#             return dist
        
#         ans = 0
#         for i in range(len(nums)-1):
#             for j in range(i+1, len(nums)):
#                 output = calculateDist(nums[i], nums[j])
#                 ans += output
        
#         return ans
        
        
        