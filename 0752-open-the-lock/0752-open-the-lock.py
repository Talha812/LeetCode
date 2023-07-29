class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def get_neighbors(state):
            neighbors = []
            for i in range(4):
                num = int(state[i])
                for change in [-1, 1]:
                    next_num = (num + change) % 10
                    next_state = state[:i] + str(next_num) + state[i + 1:]
                    neighbors.append(next_state)
            return neighbors

        start = '0000'
        
        if start in deadends:
            return -1
        
        queue = deque([(start, 0)]) # state, steps
        seen = set(deadends)
        seen.add(start)

        while queue:
            state, steps = queue.popleft()
            if state == target:
                return steps 

            for next_state in get_neighbors(state):                
                if next_state not in seen:
                    seen.add((next_state))
                    queue.append((next_state, steps + 1))
                    
        return -1