class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        
        if targetCapacity > (jug1Capacity + jug2Capacity):
            return False
        
        elif jug1Capacity == targetCapacity or jug2Capacity == targetCapacity:
            return True
        
        def findGCD(a, b):
            
            if a == b:
                return a
            
            largestMultiple = 1
            
            if a < b:
                for i in range(2, a+1):
                    if a%i == 0 and b%i == 0:
                        largestMultiple = i
            else:
                for i in range(2, b+1):
                    if a%i == 0 and b%i == 0:
                        largestMultiple = i
            
            return largestMultiple
        
        gcd = findGCD(jug1Capacity, jug2Capacity)
        
        if targetCapacity%gcd == 0:
            return True
        
        return False