class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
            
        friend = 0
        visited = set()
        i = 1
        while friend not in visited:
            visited.add(friend)
            friend += i*k
            friend = friend%n
            i += 1
            
        losers = []
        for f in range(n):
            if f not in visited:
                losers.append(f+1)
                
        return losers