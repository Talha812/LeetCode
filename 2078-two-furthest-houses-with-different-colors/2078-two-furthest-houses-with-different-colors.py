class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        
        l = 0
        r = len(colors)-1
        maxDist1 = 0
        while l <= r:
            if colors[l] != colors[r]:
                maxDist1 = max(maxDist1, abs(l-r))

            l += 1
        
        l = 0
        r = len(colors)-1
        maxDist2 = 0
        while l <= r:
            if colors[l] != colors[r]:
                maxDist2 = max(maxDist2, abs(l-r))

            r -= 1
            
        return max(maxDist1, maxDist2)