class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        
        dic = {}   #  key : value
        
        for n in arr:
            if n in dic:
                dic[n] += 1
                
            else:
                dic[n] = 1
                
        minHeap = []
        
        for key, value in dic.items():
            heappush(minHeap, (value,key))
            
        uniq = 0
        while k > 0:
            count, num = heappop(minHeap)
            if count == 1:
                k -= 1
            else:
                while count > 0 and k > 0:
                    count -= 1
                    k -= 1

                if count > 0:
                    uniq += 1

                if k == 0:
                    break
                    
        return len(minHeap) + uniq
                    
        