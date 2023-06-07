class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        
        
        stack = []
        score = 0
        
        for brkt in s:
            if brkt == "(":
                stack.append(score)
                score = 0
            else:
                if score == 0:
                    score = 1
                else:
                    score = score*2
                
                score += stack[-1]
                stack.pop()
                
        return score