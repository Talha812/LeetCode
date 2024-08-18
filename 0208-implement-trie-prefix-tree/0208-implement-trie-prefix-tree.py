class Trie:

    def __init__(self):
        self.trie = set()

    def insert(self, word: str) -> None:
        self.trie.add(word)

    def search(self, word: str) -> bool:
        if word in self.trie:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        
        for word in self.trie:
            if word[0: len(prefix)] == prefix:
                return True
        
        return False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)