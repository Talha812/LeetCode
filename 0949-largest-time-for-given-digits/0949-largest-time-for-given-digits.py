class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        
        arr.sort()
        
        for hour in range(23, -1, -1):
            for minute in range(59, -1, -1):
                curr_time = [hour//10, hour%10, minute//10, minute%10]
                sort_curr_time = sorted(curr_time)
                
                if sort_curr_time == arr:
                    return str(curr_time[0]) + str(curr_time[1]) + ":" + str(curr_time[2]) + str(curr_time[3])
            
        return ""