class MagicDictionary(object):
    def __init__(self):
        self.wordsdict = {}
        
    def buildDict(self,Dict):
        for word in Dict:
            if len(word) not in self.wordsdict:
                self.wordsdict[len(word)] = [word]
            else:
                self.wordsdict[len(word)].append(word)
                     
    def search(self,word):
        if len(word) not in self.wordsdict: 
            return False
        else:
            count = 0
            for values in self.wordsdict[len(word)]:
                count = 0
                for i in range(len(values)):
                    if values[i] == word[i]:
                        count = count + 1
                if count == len(word) - 1:
                    return True