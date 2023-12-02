class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        dic = {"a" : 0, "b" : 1, "c" : 2, "d" : 3, "e" : 4, "f" : 5, "g" : 6, "h" : 7}
        
        col = int(coordinates[1])
        row = dic[coordinates[0]]
        
        if row%2 == 0:
            if col%2 == 0:
                return True
            
            return False
        
        else:
            if col%2 == 0:
                return False
            return True