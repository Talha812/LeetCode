class Solution:
    def specialArray(self, nums: List[int]) -> int:
        
        nums.sort(reverse= True)
        
        def getGreaterEle(nums, ele):
            
            count = 0
            for i in nums:
                if i >= ele:
                    count += 1
            
            return count
        
        for i in range(len(nums)+1):  
            if i == getGreaterEle(nums, i):
                return i
            
        return -1