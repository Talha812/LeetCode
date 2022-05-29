class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        
        canBeMade = []
        
        for word in words:
            flag = True
            for char in word:
                if char not in chars or word.count(char) > chars.count(char):
                    flag = False
                    break
            
            if(flag):
                canBeMade.append(word)
                
        len_sum = 0
        for word in canBeMade:
            len_sum += len(word)
        
        return len_sum
                
                
                