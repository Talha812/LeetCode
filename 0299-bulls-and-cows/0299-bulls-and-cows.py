class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        
        
        map1 = {}
        map2 = {}
        bull = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bull += 1
            else:
                if secret[i] in map1:
                    map1[secret[i]] += 1
                else:
                    map1[secret[i]] = 1

                if guess[i] in map2:
                    map2[guess[i]] += 1
                else:
                    map2[guess[i]] = 1
                           
        cow = 0
        for k in map1:
            if k in map2:
                cow += min(map1[k], map2[k])
        
        return str(bull) + "A" + str(cow) + "B"