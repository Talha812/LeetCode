class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        
        poisonSec = 0
        for t in range(len(timeSeries)-1):
            if(timeSeries[t] + duration > timeSeries[t+1]):
                poisonSec += timeSeries[t+1] - timeSeries[t]
            else:
                poisonSec += (timeSeries[t] + duration - 1) - timeSeries[t] + 1
                
        return poisonSec+duration