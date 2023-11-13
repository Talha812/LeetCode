class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        
        max_ele = max(nums)
        ans = 0
        while k > 0:
            ans += max_ele
            max_ele += 1
            k -= 1
            
            
        return ans
            