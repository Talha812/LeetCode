class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        
        pairs = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if abs(nums[i]-nums[j]) == k:
                    pairs += 1
        
        return pairs