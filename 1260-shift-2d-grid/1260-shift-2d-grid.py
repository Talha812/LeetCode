class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        
        elements = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                elements.append(grid[i][j])
                
        k = k%(len(grid)*len(grid[0]))
        
        def reverseElements(start, end):
            while start < end:
                elements[start], elements[end] = elements[end], elements[start]
                start += 1
                end -= 1
                
        reverseElements(0, len(elements)-1)
        reverseElements(0, k-1)
        reverseElements(k, len(elements)-1)
        
        ind = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid[i][j] = elements[ind]
                ind += 1
        
        return grid