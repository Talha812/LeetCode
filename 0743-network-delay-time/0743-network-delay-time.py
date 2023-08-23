class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj_list = {i : [] for i in range(n)}
        
        for source, dest, weight in times:
            adj_list[source-1].append((dest-1, weight))
        
        
        queue = collections.deque([(k-1, 0)])
        
        visited = set()
        distance = [float("inf")]*n
        
        while queue:
            node, dist = queue.popleft()
            distance[node] = min(distance[node], dist)
            
            for neigh, distnc in adj_list[node]:
                if distnc + distance[node] < distance[neigh]:
                    queue.append((neigh, distnc + distance[node]))
        
        if max(distance) == float("inf"):
            return -1
        
        return max(distance)