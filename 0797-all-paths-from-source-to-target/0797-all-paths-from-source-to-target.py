class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        adj_list = defaultdict(int)
        for i in range(len(graph)):
            adj_list[i] = graph[i]
        
        source = 0
        destination = len(graph)-1
        queue = collections.deque()
        queue.append([source])
        ans = []

        while queue:
            temp = queue.popleft()
            if temp[-1] == destination:
                ans.append(temp[:])
            
            for neighbor in adj_list[temp[-1]]:
                queue.append(temp + [neighbor])
                
        return ans