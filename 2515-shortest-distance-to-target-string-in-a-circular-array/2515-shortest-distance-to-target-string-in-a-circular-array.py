class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        
        if target not in words:
            return -1
        
        elif words[startIndex] == target:
            return 0
        
        left = startIndex
        right = startIndex
        n = len(words)
        ans = 0
        for i in range(n):
            if words[(right + 1)%n] == target or words[(left - 1 + n) % n] == target:
                return ans+1
                        
            ans += 1
            left -= 1
            right += 1
        
        
            