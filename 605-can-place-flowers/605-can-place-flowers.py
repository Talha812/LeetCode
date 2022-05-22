class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        count = 0
        flowerbed= [0] + flowerbed + [0]
        
        for i in range(1,len(flowerbed)-1):
            if flowerbed[i-1] != 1 and flowerbed[i+1] != 1:
                if flowerbed[i] != 1:
                    flowerbed[i] = 1
                    count += 1
            
        return count >= n
    
#         count = 0
#         flowerbed = [0] + flowerbed + [0]  
        
#         for i in range(1, len(flowerbed)-1): # loop over original flowerbed (1 to len(bed)-1) as now it has 1 extra 0 at start and 1 extra 0 at end.
#             if flowerbed[i-1] == flowerbed[i] == flowerbed[i+1] == 0:
#                 count += 1
#                 flowerbed[i] = 1
                
#         return count >= n