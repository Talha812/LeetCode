class Solution:
    def longestWord(self, words: List[str]) -> str:
        
        unique = set(words)
        q = [""]
        ans = ""
        lowercase = "abcdefghijklmnopqrstuvwxyz"
        
        while q:
            word = q.pop(0)
            if(len(word) > len(ans)):
                ans = word
                
            for ch in lowercase:
                newWord = word + ch
                if newWord in unique:
                    q.append(newWord)
                    unique.remove(newWord)
        
        return ans