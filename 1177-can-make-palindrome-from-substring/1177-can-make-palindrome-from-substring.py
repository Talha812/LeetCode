class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        
        counter = 0
        running_totals = []
        for c in s:
            counter ^= 1 << (ord(c) - ord('a'))
            running_totals.append(counter)
        result = []
        for left, right, k in queries:
            frequencies = running_totals[right]
            if left > 0:
                frequencies ^= running_totals[left-1]
            result.append(k >= frequencies.bit_count() // 2)
        return result