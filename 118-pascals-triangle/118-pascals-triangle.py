class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        
        pascal_tri = [[1]]
        lastRow = []
        for i in range(1,numRows):
            newRow = []
            newRow.append(1)
            for j in range(1,i):
                newRow.append(lastRow[j]+lastRow[j-1])
            newRow.append(1)
            pascal_tri.append(newRow)
            lastRow = newRow
            
        return pascal_tri