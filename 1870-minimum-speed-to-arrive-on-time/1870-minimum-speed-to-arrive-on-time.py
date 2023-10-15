class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        
        low = 1
        high = 10e7
        canReach = False
        while low <= high:
            speed = (high+low)//2
            
            timeTaken = 0
            for i in range(len(dist)-1):
                timeTaken += ceil(dist[i]/speed)
                
            timeTaken += dist[-1]/speed
                
            if timeTaken <= hour:
                high = speed - 1
                canReach = True
            else:
                low = speed + 1
        
        if not canReach:
            return -1
        
        return int(low)