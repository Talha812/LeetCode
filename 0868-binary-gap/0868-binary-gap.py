class Solution:
    def binaryGap(self, n: int) -> int:
        
        def getBinary(n):
            return bin(n)[2:]
        
        binary = getBinary(n)
        dic = {}
        
        max_diff = 0
        
        for i in range(len(binary)):
            if binary[i] == "1" and binary[i] in dic:
                max_diff = max(i - dic[binary[i]], max_diff)
                dic[binary[i]] = i
                
            elif binary[i] == "1":
                dic[binary[i]] = i
        
        return max_diff