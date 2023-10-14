class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        
        visited = set()
        def calculate(jug1, jug2, total, filled, visited):
            if filled > total or filled < 0 or filled in visited:
                return False
            
            visited.add(filled)
            
            if filled == targetCapacity:
                return True
            
            ans1 = calculate(jug1, jug2, total, filled + jug1, visited)
            ans2 = calculate(jug1, jug2, total, filled - jug1, visited)
            ans3 = calculate(jug1, jug2, total, filled + jug2, visited)
            ans4 = calculate(jug1, jug2, total, filled - jug2, visited)
            
            return ans1 or ans2 or ans3 or ans4
        
        total = jug1Capacity + jug2Capacity
        return calculate(jug1Capacity, jug2Capacity, total, 0, visited)
            
            