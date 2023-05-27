class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
                
        stack = []
        ind = 0
        for i in pushed:
            stack.append(i)
            
            while len(stack) > 0 and popped[ind] == stack[-1]:
                stack.pop()
                ind += 1
        
        if len(stack) > 0:
            return False
        
        return True
                