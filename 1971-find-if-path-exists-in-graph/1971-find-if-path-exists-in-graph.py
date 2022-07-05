class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        
        graph = collections.defaultdict(list)
        # initialize the graph as a hash map 
        queue = collections.deque()
        # initialize the queue for Breadth First Search
        visited = set()
        # use a set to store visited nodes to avoid infinite loop. 
         
        # create the graph 
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        print(graph)
        # append the source to the queue. 
        queue.append(source)
        
        while queue:
            curr = queue.pop()
            
            if(curr not in visited):
                visited.add(curr)
            
            if curr == destination:
                return True
            
            for neighbor in graph[curr]:
                if neighbor not in visited:
                    queue.append(neighbor)
                
        return False