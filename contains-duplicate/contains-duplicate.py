class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        map = {}
        for n in nums:
            if n in map:
                map[n] += 1
            else:
                map[n] = 1
        
        for k, v in map.items():
            if v >= 2:
                return True
            
        return False