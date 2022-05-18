class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        
        dic = {}
        
        for i in arr:
            if(i/2 in dic or i*2 in dic):
                return True
            else:
                dic[i] = i/2
        
        return False
        
#         if(arr.count(0) == 2):
#             return True
        
#         for i in range(len(arr)-1):
#             for j in range(i+1, len(arr)):
#                 if(arr[i] != 0 and arr[j] != 0):
#                     if(arr[i]/arr[j] == 2 or arr[j]/arr[i] == 2):
#                         return True

        
#         return False
                    