class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        
        length = len(words)
        
        dic = {}
        for word in words:
            for ch in word:
                if ch in dic:
                    dic[ch] += 1
                else:
                    dic[ch] = 1
                    
        for k, v in dic.items():
            if v%length == 0:
                continue
            else:
                return False
            
        return True