class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        
        
        d = {}
        count = 0
        
        for i , val in enumerate(nums):
            if val not in d:
                d[val] = [i]
            else:
                for num in d[val]:
                    if (num * i ) % k == 0:
                        count += 1
                d[val].append(i)
        return count