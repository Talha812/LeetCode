class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        total_tasks = Counter(tasks)
        
        line = n + 1

        cost = 0
        while total_tasks:
            current = total_tasks.most_common(line)
            cost += len(current)
            for task, count in current:
                if total_tasks[task] > 1:
                    total_tasks[task] -= 1
                else:
                    del total_tasks[task]
                    
            if total_tasks:
                cost += line - len(current) 
                
        return cost
    
