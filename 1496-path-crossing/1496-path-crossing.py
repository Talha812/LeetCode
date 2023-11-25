class Solution:
    def isPathCrossing(self, path: str) -> bool:
        
        visited = set()
        
        point = (0, 0)
        for d in path:            
            visited.add(point)
            
            if d == "E":
                point = (point[0]+1, point[1])
            
            elif d == "W":
                point = (point[0]-1, point[1])
            
            elif d == "N":
                point = (point[0], point[1]+1)
            
            elif d == "S":
                point = (point[0], point[1]-1)
        
            if point in visited:
                return True
        
        
        return False