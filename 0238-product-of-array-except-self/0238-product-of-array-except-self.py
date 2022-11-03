class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        leftPro = []
        rightPro = []
        
        left = 1
        
        for i in range(len(nums)):
            leftPro.append(left)
            left = left * nums[i]
            
        right = 1
        for i in range(len(nums)-1, -1, -1):
            rightPro.append(right)
            right = right * nums[i]
        
        #print(leftPro, rightPro)
        rev = rightPro[::-1]
        #print(rev)
        ans = []
        for i in range(len(nums)):
            ans.append(leftPro[i]*rev[i])
            
        return ans