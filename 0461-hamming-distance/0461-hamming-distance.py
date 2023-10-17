class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        
        XOR = x^y
        
        bin_XOR = bin(XOR)[2:]
        
        return bin_XOR.count("1")