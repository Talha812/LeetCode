class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:

        n = len(points)
        
        rec = [[] for i in range(n)] # => [[], [], [], [], []]
        
        for i in range(n):
            for j in range(i+1, n):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                
                rec[i].append((dist, j))
                rec[j].append((dist, i))
                
        # print(rec)
        visited = [False] * n
        
        minHeap = rec[0]   # [(dist, point)]
        
        visited[0] = True
        heapify(minHeap)
        
        cost = 0
        point_vis = 0
        
        while point_vis < n -1:
            dist, ind = heappop(minHeap)
            
            if not visited[ind]:
                visited[ind] = True
                cost += dist
                
                point_vis += 1
                
                for further_point in rec[ind]:
                    heappush(minHeap, further_point)
            
        return cost
                
        