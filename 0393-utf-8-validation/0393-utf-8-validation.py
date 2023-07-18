class Solution:
    def validUtf8(self, data: List[int]) -> bool:
                
        noOfBytes = 0
        i = 0
        while i < len(data):
            
            numOfBytes = 0
            
            if (data[i] & 0x80) == 0:
                noOfBytes = 0
                i += 1
                continue
            
            elif (data[i] & 0xE0) == 0xC0:
                noOfBytes = 2
                
            elif (data[i] & 0xF0) == 0xE0:
                noOfBytes = 3
            
            elif (data[i] & 0xF8) == 0xF0:
                noOfBytes = 4
            
            else:
                 return False
                
            i += 1
            noOfBytes -= 1
            while (noOfBytes > 0 and i < len(data)):
                if (data[i] & 0xC0) != 0x80:
                    return False
                
                i += 1
                noOfBytes -= 1
        
        if noOfBytes != 0:
            return False
        
        return True
            