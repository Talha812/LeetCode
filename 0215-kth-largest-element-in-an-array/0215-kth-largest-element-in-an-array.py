class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        maxHeap = []
        for i in nums:
            heappush(maxHeap, (-1*i))
        
        val = float('inf')
        while k > 0:
            val = -1*heappop(maxHeap)
            k -= 1
        
        return val