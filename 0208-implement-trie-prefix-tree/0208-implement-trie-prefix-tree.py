class Trie:

    def __init__(self):    
        self.words = []

    def insert(self, word: str) -> None:
        self.words.append(word)
        
    def search(self, word: str) -> bool:
        if len(self.words) == 0:
            return False
        
        for w in self.words:
            if w == word:
                return True
        
        return False
        
    def startsWith(self, prefix: str) -> bool:
        if len(self.words) == 0:
            return False
         
        for w in self.words:
            if len(w) >= len(prefix):
                if w[0:len(prefix)] == prefix:
                    return True
            
        return False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)