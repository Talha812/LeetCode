class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        
        dic = {}
        
        pairs = 0
        for i in range(len(nums)):  
            if nums[i]-k in dic:
                pairs += dic[nums[i]-k]
            if nums[i]+k in dic:
                pairs += dic[nums[i]+k]
                
            if nums[i] not in dic:
                dic[nums[i]] = 1
            else:
                dic[nums[i]] += 1
                        
        return pairs