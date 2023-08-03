class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        
        i = 0
        max_score = -1
        
        for j in range(i+1, len(values)):
            max_score = max(max_score, values[i] + values[j] + i - j)
            
            if values[i] < values[j] - i + j:
                i = j
        
        return max_score
        
#         max_score = -1
        
#         for i in range(len(values)):
#             for j in range(i+1, len(values)):
#                 if (values[i] + values[j] + i - j) > max_score:
#                     max_score = values[i] + values[j] + i - j
        
#         return max_score
    
    