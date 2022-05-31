class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        
        def split_Sentence(self, sentence):
            array = []
            sentence += " "
            word = ""
            for i in range(len(sentence)):
                if(sentence[i] == " "):
                    array.append(word)
                    word = ""
                else:
                    word += sentence[i]
            return array
        
        maximum = 0
        
        for sentence in sentences:
            splitted = split_Sentence(self,sentence)
            if(len(splitted) > maximum):
                maximum = len(splitted)
        
        return maximum
            