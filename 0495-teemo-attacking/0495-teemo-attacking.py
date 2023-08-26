class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        
        poisoned = 0
        for t in range(len(timeSeries)-1):
            if(timeSeries[t] + duration > timeSeries[t+1]):
                poisoned += timeSeries[t+1] - timeSeries[t]
            else:
                poisoned += (timeSeries[t] + duration - 1) - timeSeries[t] + 1
                
        return poisoned+duration