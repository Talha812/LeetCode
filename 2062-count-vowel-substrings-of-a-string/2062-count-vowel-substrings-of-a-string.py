class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        ans = 0
        for i in range(len(word)):
            vowels = set()
            for j in range(i, len(word)):
                if word[j] not in "aeiou":
                    break
                    
                if word[j] in "aeiou":
                    vowels.add(word[j])
                    if len(vowels) == 5:
                        ans += 1
                        
        return ans