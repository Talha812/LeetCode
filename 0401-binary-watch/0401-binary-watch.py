class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        
        def lightsOnCount(n):
            binn = bin(n)[2:]
            return binn.count("1")
        
        ans = []
        for h in range(12):
            for m in range(60):
                if lightsOnCount(h) + lightsOnCount(m) == turnedOn:
                    if m < 10:
                        ans.append(str(h) + ":0" + str(m))
                    else:
                        ans.append(str(h) + ":" + str(m))
        
        return ans