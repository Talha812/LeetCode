class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        
        def getMinutes(time):
            return (60*int(time[0:2])) + int(time[3:])
        
        curr_min = getMinutes(current)
        corr_min = getMinutes(correct)
        
        required = corr_min - curr_min
        
        operations = 0
        if required >= 60:
            operations += required//60
            required = required%60
        
        if required >= 15:
            operations += required//15
            required = required%15
        
        if required >= 5:
            operations += required//5
            required = required%5
            
        operations += required
        
        return operations