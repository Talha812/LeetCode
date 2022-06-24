class Solution:
    def reverseVowels(self, s: str) -> str:
        
        l = list(s)
        #print(l)
        
        low = 0
        high = len(l)-1
        
        while(low<high):
    
            if(l[low] != "a" and l[low] != "A" and l[low] != "e" and l[low] != "E" and l[low] != "i" and l[low] != "I" and l[low] != "o" and l[low] != "O" and l[low] != "u" and l[low] != "U"):
                low += 1 
                
            elif(l[high] != "a" and l[high] != "A" and l[high] != "e" and l[high] != "E" and l[high] != "i" and l[high] != "I" and l[high] != "o" and l[high] != "O" and l[high] != "u" and l[high] != "U"):
                high -= 1 
            
            else:
                temp = l[low]
                l[low] = l[high]
                l[high] = temp
                low += 1
                high -= 1
        print(l)
        
        return "".join(l)