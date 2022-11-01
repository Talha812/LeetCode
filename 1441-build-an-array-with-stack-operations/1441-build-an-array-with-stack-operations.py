class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        
        result = []
        i = 0           #indexes         
        for num in range(1, n+1):   #picking numbers
            if (target[i] == num):
                result.append("Push")
                i+=1 
                
            else:
                result.append("Push")
                result.append("Pop")
                
            if (num == target[len(target)-1]):
                break
        
        return result
    
    