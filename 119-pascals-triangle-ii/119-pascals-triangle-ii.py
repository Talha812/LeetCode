class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        if rowIndex == 0:
            return [1]
                
        if rowIndex == 1:
            return [1,1]
        
        res = [[1]]
        
        for x in range(1, rowIndex+1): 
            # Build a new row.
            row = []
            row.append(1)
            if x > 1:
                for y in range(1, x): 
                    row.append(lastRow[y] + lastRow[y - 1])
            row.append(1)
            
            lastRow = row
            
            res.append(list(row))
        print(res)
        
        return res[rowIndex]
        
         