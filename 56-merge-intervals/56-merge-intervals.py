class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals=sorted(intervals)
        output=[]
        output.append(intervals[0])
        for i in range(1,len(intervals)):
            if output[-1][1]>=intervals[i][0]:
                output[-1][1]=max(output[-1][1],intervals[i][1])
            else:
                output.append(intervals[i])
        return output

    
    
# 1   2   3   4   5   6   7   8   9     10    11  12  13  14  15  16  17  18