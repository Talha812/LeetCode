class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        
        if int(coordinates[-1])%2!=0:
            if (ord(coordinates[0])-ord('a'))%2==0:
                return False
            else: return True
        else:
            if (ord(coordinates[0])-ord('a'))%2!=0:
                return False
            else: return True