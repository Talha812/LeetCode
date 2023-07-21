class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        
        prevError= float("inf")
        ans = 0
        for i in nums:
            error = abs(i)
            if error < prevError:
                prevError = error
                ans = i
            elif error == prevError:
                ans = max(i, ans)
        
        return ans