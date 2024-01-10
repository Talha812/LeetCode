class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        
        colums = [""] * len(strs[0])
        
        for i in range(len(strs)):
            for j in range(len(strs[0])):
                colums[j] += strs[i][j]
                
        toDelete = 0
        for col in colums:
            flag = True
            
            for i in range(len(col)-1):
                if ord(col[i]) > ord(col[i+1]):
                    flag = False
                    break
            
            if not flag:
                toDelete += 1
                
        return toDelete