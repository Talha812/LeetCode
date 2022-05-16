class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        array_1 = []
        array_2 = []
        
        for i in range(len(s)):
            if(s[i] != "#"):
                array_1.append(s[i])
            elif(len(array_1) > 0):
                array_1.pop()
        
        for i in range(len(t)):
            if(t[i] != "#"):
                array_2.append(t[i])
            elif(len(array_2) > 0):
                array_2.pop()
        
        return array_1 == array_2
        