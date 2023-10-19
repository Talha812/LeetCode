class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        
        ans, chainEnd = 0, float("-inf")
        pairs.sort(key = lambda x: x[1])

        for left, right in pairs:
            if left > chainEnd:
                ans += 1
                chainEnd = right

        return ans
        