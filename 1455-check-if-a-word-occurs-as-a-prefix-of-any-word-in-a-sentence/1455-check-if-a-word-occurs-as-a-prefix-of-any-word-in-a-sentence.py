class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        
        array = sentence.split(" ")
        
        for i in range(len(array)):
            if(searchWord == array[i][0:len(searchWord)]):
                return (i+1)
            
        return -1