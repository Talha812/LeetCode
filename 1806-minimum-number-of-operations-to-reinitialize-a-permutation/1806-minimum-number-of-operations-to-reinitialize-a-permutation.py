class Solution:
    def reinitializePermutation(self, n: int) -> int:
        
        perm = []
        for i in range(0, n):
            perm.append(i)

        newPerm = perm
        operation = 0
        while(True):
            a = []
            for i in range(len(newPerm)):
                if i % 2 == 0:
                    a.append(newPerm[i // 2])
                
                elif i % 2 == 1:
                    a.append(newPerm[n // 2 + (i - 1) // 2])

            operation = operation + 1

            newPerm = a

            if newPerm == perm:
                return operation