class Solution:
#     def captureForts(self, forts: List[int]) -> int:
        
#         # forward
        
#         i = 0
#         max_cap_f = 0
#         while i < len(forts):
#             if forts[i] == 1:
#                 count_0 = 0
#                 i += 1
#                 while i < len(forts):
#                     if forts[i] == 0:
#                         count_0 += 1
                    
#                     if forts[i] == 1 or forts[i] == -1:
#                         break
                    
#                     i += 1
                    
#                 max_cap_f = max(max_cap_f, count_0)
            
#             i += 1
        
        
#         # backward
        
#         i = len(forts)-1
#         max_cap_b = 0
#         while i >= 0:
#             if forts[i] == 1:
#                 count_0 = 0
#                 i += 1
#                 while i >= 0:
#                     if forts[i] == 0:
#                         count_0 += 1
                    
#                     if forts[i] == 1 or forts[i] == -1:
#                         break
                
#                     i -= 1
                
#                 max_cap_b = max(max_cap_b, count_0)
                
#             i -= 1
        
#         return max(max_cap_f, max_cap_b)
    
    
    
    def captureForts(self, forts: List[int]) -> int:
        
        # move forward
        max_captured = 0
        for i in range(len(forts)):
            captured = 0
            if forts[i] == 1:
                i += 1
                # start travelling
                while i < len(forts) and forts[i] == 0:
                    captured += 1
                    i += 1
                if i < len(forts) and forts[i] == -1:
                    max_captured = max(max_captured, captured)
        
        # move backward
        for i in range(len(forts)-1, -1, -1):
            captured = 0
            if forts[i] == 1:
                i -= 1
                # start travelling
                while i >= 0 and forts[i] == 0:
                    captured += 1
                    i -= 1
                if i >= 0 and forts[i] == -1:
                    max_captured = max(max_captured, captured)
        
        return max_captured