class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        
        stack = []
        
        for i in pushed:
            stack.append(i)

            while len(stack)!=0 and len(popped)!=0 and stack[-1] == popped[0]:
                stack.pop()
                popped.pop(0)

        return len(stack)==0 