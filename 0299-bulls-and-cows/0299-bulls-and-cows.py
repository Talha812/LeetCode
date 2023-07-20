class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        
#         bull = 0
#         dic1 = {}
#         dic2 = {}
        
#         for i in range(len(secret)):
#             if secret[i] == guess[i]:
#                 bull += 1
#             else:
#                 if secret[i] in dic1:
#                     dic1[secret[i]] += 1
#                 else:
#                     dic1[secret[i]] = 1
                
#                 if guess[i] in dic2:
#                     dic2[guess[i]] += 1
#                 else:
#                     dic2[guess[i]] = 1
        
#         cow = 0
#         for k in dic1:
#             if k in dic2:
#                 cow += min(dic1[k], dic2[k])
        
#         return str(bull) + "A" + str(cow) + "B"


        bull = 0
        dic = {}
        
        for i in range(len(secret)):
            if secret[i] in dic:
                dic[secret[i]] += 1
            else:
                dic[secret[i]] = 1
        cow = 0
        for i in range(len(guess)):
            if guess[i] == secret[i]:
                bull += 1
                dic[secret[i]] -= 1
                            
        cow = 0
        for i in range(len(guess)):
            if guess[i] in dic and dic[guess[i]] > 0 and guess[i] != secret[i]:
                cow += 1
                dic[guess[i]] -= 1
        
        return str(bull) + "A" + str(cow) + "B"