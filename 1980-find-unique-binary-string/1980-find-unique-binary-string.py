class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        
#         if len(nums) == 1:
#             if nums[0] == "1":
#                 return "0"
#             else:
#                 return "1"
        
#         ans = 0
#         for n in nums:
#             ans = ans^int(n, base=2)
        
#         return bin(ans)[2:]
    
    
        seen=set(nums)
        n=len(nums)
        
        for i in range(0, 2**(n+1)): 
            Binary = bin(i)[2:]
            if (Binary == "0" or Binary == "1") and (("0"*(len(nums[0])-1)) + Binary) not in seen:
                return ("0"*(len(nums[0])-1)) + Binary
            
            if Binary not in seen and len(Binary) == len(nums[0]):
                return Binary