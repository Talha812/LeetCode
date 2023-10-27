class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
                
        # clockwise
        clockwise_dist = 0
        
        if start < destination:
            for i in range(start, destination):
                clockwise_dist += distance[i]
        elif destination < start:
            for i in range(start-1, destination-1, -1):
                clockwise_dist += distance[i]
                
        total_dist = sum(distance)
        
        anti_clock_dist = total_dist - clockwise_dist
        
        return min(anti_clock_dist, clockwise_dist)
    