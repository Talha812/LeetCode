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
    
    # T = 1 + 1 + 1 + (N*N) + 1
    # T = N^2 + 4
    # T = O(N^2)
    
    #nlog(n) + N + N^2
    #  N^2 
    # Better --> Worst
    # 1 -> log(n) -> nlog(n) -> N -> N^2 -> N^3 -> 2^n -> n!
    
    