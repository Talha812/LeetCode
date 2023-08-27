class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        
        dic = {}
        for point in points:
            if tuple(point) in dic:
                dic[tuple(point)] += 1
            else:
                dic[tuple(point)] = 1
        
        if len(dic) < 3:
            return False
        
        x1, y1 = points[0]
        x2, y2 = points[1]
        x3, y3 = points[2]
        
        
        if x1-x2 == 0 and x2-x3 == 0:
            return False
        
        if y1-y2 == 0 and y2-y3 == 0:
            return False
        
        if (x1-x2 == 0 and x2-x3 != 0) or (x1-x2 != 0 and x2-x3 == 0):
            return True
        
        if (y1-y2 == 0 and y2-y3 != 0) or (y1-y2 != 0 and y2-y3 == 0):
            return True
        
        if (y2-y1)/(x2-x1) == (y3-y2)/(x3-x2):
            return False
        
        return True