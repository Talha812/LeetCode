class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        
        ans = []
        
        for ind in range(len(nums[0])):
            doExist = True
            for j in range(1,len(nums)):
                if(nums[0][ind] not in nums[j]):
                    doExist = False
                    break
            
            if doExist:
                ans.append(nums[0][ind])
                
        ans.sort()
        
        return ans
    
    