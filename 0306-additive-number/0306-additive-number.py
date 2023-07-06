class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        
        
        for i in range(1, len(num)):        # get first num
            for j in range(i+1, len(num)):  # get sec num
                if num[0] == "0" and i > 1:
                    break

                if num[i] == "0" and j > i + 1:
                    break
                
                n1 = num[0 : i]
                n2 = num[i : j]
                
                k = j
                while k < len(num): #get third num
                    
                    n3 = int(n1) + int(n2)
                    if num[k:len(num)].startswith(str(n3)):
                        n1 = n2
                        n2 = n3
                        k += len(str(n3))
                        
                    else:
                        break
                        
                if k == len(num):
                    return True
        
        return False