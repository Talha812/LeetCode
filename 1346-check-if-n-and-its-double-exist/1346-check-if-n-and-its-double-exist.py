class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        
        dic = {}
        
        for i in arr:
            if(i/2 in dic or i*2 in dic):
                return True
            else:
                dic[i] = i/2
        
        return False
                    