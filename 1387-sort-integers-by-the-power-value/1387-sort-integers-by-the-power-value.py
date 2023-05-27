class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        
        def transformCount(num):
            count = 0
            while num > 1:
                if num%2 == 0:
                    num = num//2
                else:
                    num = (3*num) + 1
                count += 1
            
            return count
        
        rec = []
        while lo <= hi:
            c = transformCount(lo)
            rec.append((c, lo))
            lo += 1
        
        rec.sort()
        return rec[k-1][1]