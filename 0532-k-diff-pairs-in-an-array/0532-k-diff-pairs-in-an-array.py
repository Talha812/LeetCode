class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        
        ans = 0
        visited = set()
        dic = {}
        for n in nums:
            if n in dic:
                dic[n] += 1
            else:
                dic[n] = 1
        
        if k == 0:
            for key, val in dic.items():
                if val > 1:
                    ans += 1
            
            return ans
            
        
        for key, val in dic.items():
            add = key + k
            sub = key - k
            
            pair1 = (key, add)
            pair2 = (key, sub)
            
            if add in dic and pair1 not in visited and (add, key) not in visited:
                ans += 1
                visited.add(pair1)
                visited.add((add, key))
            
            if sub in dic and pair2 not in visited and (sub, key) not in visited:
                ans += 1
                visited.add(pair2)
                visited.add((sub, key))
                
        return ans
        
#         ans = 0
#         visited = set()
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
                
#                 if abs(nums[i] - nums[j]) == k and (nums[i], nums[j]) not in visited and (nums[j], nums[i]) not in visited:
#                     ans += 1
#                     visited.add((nums[i], nums[j]))
#                     visited.add((nums[j], nums[i]))

#         return ans