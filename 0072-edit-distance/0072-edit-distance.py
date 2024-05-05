class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        def calculate(w1, w2, i, j, memo):
            if i == len(w1):
                return len(w2) - j
            
            elif j == len(w2):
                return len(w1) - i
            
            if (i,j) in memo:
                return memo[(i,j)]
            
            elif w1[i] == w2[j]:
                return calculate(w1, w2, i+1, j+1, memo)
            
            else:
                delete = calculate(w1, w2, i+1, j, memo)
                replace = calculate(w1, w2, i+1, j+1, memo)
                insert = calculate(w1, w2, i, j+1, memo)
                
                output = 1 + min(delete, replace, insert)
            
                memo[(i,j)] = output
                return memo[(i,j)]
        
        memo = {}
        ans = calculate(word1, word2, 0, 0, memo)
        
        return ans