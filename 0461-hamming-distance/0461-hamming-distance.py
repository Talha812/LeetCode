class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        
        XOR = x^y
        
        count = 0
        while XOR > 0:
            and_ans = XOR & 1
            count += and_ans
            XOR >>= 1
        
        return count
    
#         bin_XOR = bin(XOR)[2:]
        
#         return bin_XOR.count("1")
