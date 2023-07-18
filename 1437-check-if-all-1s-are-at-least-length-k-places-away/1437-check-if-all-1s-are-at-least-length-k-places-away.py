class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        
        rec = -1
        
        for i in range(len(nums)):
            if nums[i] == 1 and rec == -1:
                rec = i
            
            elif nums[i] == 1:
                if i - rec - 1 < k:
                    return False
                else:
                    rec = i
        
        return True