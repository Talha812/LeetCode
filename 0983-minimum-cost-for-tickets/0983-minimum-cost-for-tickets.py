class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        def calculate(days, costs, curr_ind, memo):
            
            if curr_ind >= len(days):
                return 0
            
            if memo[curr_ind] != -1:
                return memo[curr_ind]
            
            # for 1 day
            cost1Days = costs[0] + calculate(days, costs, curr_ind+1, memo)
            
            # for 7 days
            next_ind = curr_ind
            while next_ind < len(days) and days[next_ind] <= days[curr_ind]+6:
                next_ind += 1
            
            cost7Days = costs[1] + calculate(days, costs, next_ind, memo)
            
            # for 30 days
            next_ind = curr_ind
            while next_ind < len(days) and days[next_ind] <= days[curr_ind]+29:
                next_ind += 1
            
            cost30Days = costs[2] + calculate(days, costs, next_ind, memo)
            
            memo[curr_ind] = min(cost1Days, cost7Days, cost30Days)
            return memo[curr_ind]
        
        memo = [-1]*len(days)
        
        return calculate(days, costs, 0, memo)