class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        minHeap = []
        
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                heappush(minHeap, matrix[i][j])
        
        ans = 0
        while k > 0:
            if minHeap:
                ans = heappop(minHeap)
            
            k -= 1
            
        return ans