class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
        if(len(nums) == 1):
            return True
        
        arrIs = ""
        
        if(nums[0] < nums[len(nums)-1]):
            arrIs = "incre"
                
        else:
            arrIs = "decre"
        
        if(arrIs == "incre"):
            for i in range(len(nums)-1):
                if(nums[i+1]<nums[i]):
                    return False
                
        else:
            for i in range(len(nums)-1):
                if(nums[i+1]>nums[i]):
                    return False
            
            
        return True