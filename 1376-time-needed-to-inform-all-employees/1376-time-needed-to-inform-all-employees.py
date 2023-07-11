class Solution:
    def numOfMinutes(self, n, headID, manager, informTime):
        
        if n == 1:
            return informTime[0]
        
        head_emp = {}
        
        for i in range(len(manager)):                
            if manager[i] not in head_emp:
                head_emp[manager[i]] = [(i, informTime[manager[i]])]
                
            else:
                head_emp[manager[i]].append((i, informTime[manager[i]]))
        
        #print(head_emp)
        
        queue = head_emp[headID]
        #print(queue)
        
        max_time = 0
        while queue:
            mana_ger, time = queue.pop(0)
            #print(mana_ger, time)
            
            if mana_ger in head_emp:
                for e, t in head_emp[mana_ger]:
                    queue.append((e, t+time))
                    max_time = max(max_time, t+time)
            
            else:
                max_time = max(max_time, time)
            
        return max_time

            