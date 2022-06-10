class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if(len(s) != len(goal)):
            return False
        
        string = s
        shift = 0
        while(shift < len(s)):
            if(string == goal):
                return True
            string = string[1:len(s)] + string[0]
            shift += 1
        
        return False