class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        
        visited = set()
        for n in nums:
            if n in visited:
                visited.remove(n)
            else:
                visited.add(n)
            
        ans = list(visited)
        
        return ans