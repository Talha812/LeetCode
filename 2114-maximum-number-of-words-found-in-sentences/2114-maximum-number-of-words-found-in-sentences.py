class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        
        maximum = 0
        
        for sentence in sentences:
            splitted = sentence.split(" ")
            if(len(splitted) > maximum):
                maximum = len(splitted)
        
        return maximum
            