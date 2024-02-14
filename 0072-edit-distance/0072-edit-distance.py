class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
    
        def checkPossibilities(word1, word2, i, j, memo):
            
            if j == len(word2):
                return len(word1) - i
            
            elif i == len(word1):
                return len(word2) - j
                
            if (i,j) in memo:
                return memo[(i,j)]
            
            elif word1[i] == word2[j]:
                return checkPossibilities(word1, word2, i+1, j+1, memo)
            
            else:
                output = min(
                    checkPossibilities(word1, word2, i+1, j, memo),  # Delete
                    checkPossibilities(word1, word2, i, j+1, memo),  # insert
                    checkPossibilities(word1, word2, i+1, j+1, memo)  # Replace
                )
                
                memo[(i,j)] = 1 + output
                return memo[(i,j)] 
        
        memo = {}
        return checkPossibilities(word1, word2, 0, 0, memo)
        
        
        
        