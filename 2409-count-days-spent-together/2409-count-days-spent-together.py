class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
            
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        def getDate(date):
            month = int(date[:2])
            days = int(date[3:])
            return sum(month_days[: month - 1]) + days
    
        start = getDate(max(arriveAlice, arriveBob))
        end = getDate(min(leaveAlice, leaveBob))
    
        return max(0, end - start + 1)
    
        