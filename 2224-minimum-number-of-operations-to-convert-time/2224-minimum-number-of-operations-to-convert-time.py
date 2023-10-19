class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        
        def getMinutes(time):
            return (60*int(time[0:2])) + int(time[3:5])
        
        curr_min = getMinutes(current)
        corr_min = getMinutes(correct)
        
        required = corr_min - curr_min
        
        operations = 0
        while required > 0:
            
            if required >= 60:
                operations += 1
                required -= 60
        
            elif required >= 15:
                operations += 1
                required -= 15
        
            elif required >= 5:
                operations += 1
                required -= 5
            
            elif required >= 1:
                operations += 1
                required -= 1
        
        return operations