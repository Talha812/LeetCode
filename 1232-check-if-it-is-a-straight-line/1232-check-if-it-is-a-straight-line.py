class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        
        x1 = coordinates[0][0]
        y1 = coordinates[0][1]
        
        x2 = coordinates[1][0]
        y2 = coordinates[1][1]
        
        slope = 0
        if x2 != x1:
            slope = (y2-y1)/(x2-x1)
        else:
            slope = float("inf")
        
        for i in range(1, len(coordinates)-1):
            x1 = coordinates[i][0]
            y1 = coordinates[i][1]
            
            x2 = coordinates[i+1][0]
            y2 = coordinates[i+1][1]
            if x1 != x2:
                newSlope = (y2-y1)/(x2-x1)
                if slope != newSlope:
                    return False
            else:
                if slope != float("inf"):
                    return False
        
        return True
        
        