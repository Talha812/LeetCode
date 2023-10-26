class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        
        def calculateDays(date):
            start = 1900

            curr_y, curr_m, curr_d = date.split("-")
            
            total_days = 0
            for y in range(start, int(curr_y)):
                total_days += 365
                if y%100 == 0:
                    if y%400 == 0:
                        total_days += 1
                else:
                    if y%4 == 0:
                        total_days += 1
            
            for m in range(int(curr_m)):
                if m == 2:
                    total_days += 28
                    if int(curr_y)%100 == 0:
                        if int(curr_y)%400 == 0:
                            total_days += 1
                    else:
                        if int(curr_y)%4 == 0:
                            total_days += 1
                            
                elif m in [1,3,5,7,8,10,12]:
                    total_days += 31
                    
                elif m in [4,6,9,11]:
                    total_days += 30
            
            total_days += int(curr_d)
            
            return total_days
        
        return abs(calculateDays(date1) - calculateDays(date2))
    