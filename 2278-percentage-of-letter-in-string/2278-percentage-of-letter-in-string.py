class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        
        letter_count = s.count(letter)
        
        perc = (letter_count*100)//len(s)
        
        return perc