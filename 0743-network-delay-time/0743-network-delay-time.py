class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = {i : [] for i in range(n)}
        
        for src, dest, time in times:
            adj_list[src-1].append((dest-1, time))
            
        visited = set()
        
        all_time = [float("inf")]*n  
        
        queue = collections.deque([(k-1, 0)]) 
        
        while queue:
            curr_node, time = queue.popleft()
            
            all_time[curr_node] = min(time, all_time[curr_node])
            
            visited.add(curr_node)
            
            for neigh, neigh_time in adj_list[curr_node]:
                if neigh_time + all_time[curr_node] < all_time[neigh]:
                    queue.append((neigh, neigh_time + all_time[curr_node]))
            
        if len(visited) != n:
            return -1
        
        return max(all_time)