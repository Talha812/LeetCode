class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
#         if word == word.upper():
#             return True
        
#         elif word == word.lower():
#             return True
        
#         elif word == word.capitalize():
#             return True
        
#         return False
    
        return word == word.upper() or word == word.lower() or word == word.capitalize()