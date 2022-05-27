class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        dic = {}
        s = s.split()
        if len(pattern) != len(s):
            return False
        
        for i in range(len(pattern)):
            char, word = pattern[i], s[i]
            if char not in dic:
                if word in dic.values():
                    return False
                dic[char] = word
            elif dic[char] != word:
                return False
        return True
        