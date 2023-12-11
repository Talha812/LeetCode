class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        
        def reverse(n):
            if n == 0:
                return n
            
            ans = ""
            
            while n > 0:
                rem = n%10
                ans = ans + str(rem)
                n = n//10
            
            return int(ans)
        
        arr = []
        
        for i in range(len(nums)):
            arr.append(nums[i] - reverse(nums[i]))
            
        dic = {}
        ans = 0
        for n in arr:
            if n in dic:
                ans += dic[n]
                dic[n] += 1
            else:
                dic[n] = 1
        
        return ans%(10**9 + 7)
        
                