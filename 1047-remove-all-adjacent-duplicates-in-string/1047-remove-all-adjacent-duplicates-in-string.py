class Solution:
    def removeDuplicates(self, s: str) -> str:
        
        stack = []
        
        for i in range(len(s)):
            if(i == 0):
                stack.append(s[i])
            elif(len(stack) != 0 and stack[-1] == s[i]):
                stack.pop()
            else:
                stack.append(s[i])
        
        return "".join(stack)