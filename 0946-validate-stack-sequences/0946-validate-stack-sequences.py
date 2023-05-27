class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        def reverse(popped):
            i = 0
            j = len(popped)-1
            
            while i < j:
                popped[i], popped[j] = popped[j], popped[i]
                i += 1
                j -= 1
            
            return popped
        
        popped = reverse(popped)
        
        stack = []
        for i in pushed:
            stack.append(i)
            
            while len(stack) > 0 and popped[-1] == stack[-1]:
                stack.pop()
                popped.pop()
        
        if len(stack) > 0:
            return False
        
        return True
                