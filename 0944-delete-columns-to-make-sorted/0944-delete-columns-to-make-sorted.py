class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        
        output = [[] for i in range(0, len(strs[0]))]

        for i in range(0, len(strs)):
            for j in range(0, len(strs[i])):
                output[j].append(strs[i][j])

        count = 0
        for i in output:
            isOrder = True
            prev = i[0]
            for j in range(1, len(i)):
                if prev > i[j]:
                    isOrder = False
                prev = i[j]
            if not isOrder:
                count += 1 
        return count