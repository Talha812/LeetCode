class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        dic = {0:1}
        s = 0
        ans = 0
        for n in nums:
            s += n
            if s-goal in dic:
                ans += dic[s-goal]
            
            if s in dic:
                dic[s] += 1
            else:
                dic[s] = 1
            
        return ans