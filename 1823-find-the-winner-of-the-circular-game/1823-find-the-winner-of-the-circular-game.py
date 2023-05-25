class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        players = [1]*n
        eleminated = 0
        
        i = 0
        while True:
            cnt = k-1
            while (cnt>0 or players[i]<0):
                
                if(players[i] < 0):
                    i += 1
                    i = i%n
                    continue
                    
                cnt -= 1
                i += 1
                i = i%n
            
            if(eleminated == n-1):
                return i+1
            
            players[i] = -1
            eleminated += 1
            i += 1
            i = i%n