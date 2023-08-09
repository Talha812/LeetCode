class WordDictionary:

    def __init__(self):
        self.store = []

    def addWord(self, word: str) -> None:
        if word not in self.store:
            self.store.append(word)

    def search(self, word: str) -> bool:
        if word in self.store:
            return True
        elif '.' not in word:
            return False
        else:
            dot_positions = []
            for idx, char in enumerate(word):
                if char == '.':
                    dot_positions.append(idx)
                    
            for s in self.store:
                if len(s) == len(word):
                    s_list = list(s)
                    for i in dot_positions:
                        s_list[i] = '.'
                    if s_list == list(word):
                        return True
            return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)