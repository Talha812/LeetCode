class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        
        count = 0
        for i in words:
            if (i == s[0:len(i)]):
                count += 1
        
        return count