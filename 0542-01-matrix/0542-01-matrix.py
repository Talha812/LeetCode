class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        queue = collections.deque()
        visited = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        ans = [[0] * len(mat[0]) for i in range(len(mat))]
        #print(ans)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    queue.append((i, j))
                    visited.add((i,j))

        dist = 1
        while queue:
            size = len(queue)
            for i in range(size):
                r, c = queue.popleft()
                for direction in directions:
                    new_row = direction[0] + r
                    new_col = direction[1] + c
                    
                    if new_row < len(mat) and new_row >= 0 and new_col < len(mat[0]) and new_col >= 0 and (new_row, new_col) not in visited:
                        ans[new_row][new_col] = dist
                        visited.add((new_row, new_col))
                        queue.append((new_row, new_col))
            
            dist += 1
        
        return ans