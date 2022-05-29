class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        
        codes = {
            "a":".-", "b":"-...", "c":"-.-.", "d":"-..", "e":".", "f":"..-.", "g":"--.", "h":"....", "i":"..", "j":".---", "k":"-.-", "l":".-..", "m":"--", "n":"-.", "o":"---", "p":".--.", "q":"--.-", "r":".-.", "s":"...", "t":"-", "u":"..-", "v":"...-", "w":".--", "x":"-..-", "y":"-.--", "z":"--.."
        }
        
        transformations = []
        for word in words:
            code = ""
            for i in word:
                code += codes[i]
            
            transformations.append(code)
        
        unique_trans = []
        for i in transformations:
            if i not in unique_trans:
                unique_trans.append(i)
        
        return len(unique_trans)
    
    
            