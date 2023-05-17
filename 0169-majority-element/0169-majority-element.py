class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        
        dic = {}
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        
        
        for num in dic:
            if dic[num] > math.floor(len(nums)/2):
                return num
    
        