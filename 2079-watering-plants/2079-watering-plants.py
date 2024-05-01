class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        
        
        if capacity < plants[0]:
            return -1              
        
        steps = 0
        water_can = capacity
        i=0
        
        while i < len(plants):
            if water_can >= plants[i]:
                steps += 1
                water_can -= plants[i]
                i += 1
            else:
                steps += i*2
                water_can = capacity
                
        return steps
