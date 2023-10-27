class Solution:
    def dayOfYear(self, date: str) -> int:
        
        def isLeap(year):
            if year % 4 == 0:
                if year % 100 == 0:
                    if year % 400 == 0:
                        return True
                    else:
                        return False
                else:
                    return True
            else:
                return False
        
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        year, month, day = date.split("-")
        year, month, day = int(year), int(month), int(day)
        
        total_days = 0
        
        for i in range(month-1):
            total_days += days[i]
        
        total_days += day
        
        if isLeap(year) and month > 2:
            total_days += 1
                
        return total_days
        