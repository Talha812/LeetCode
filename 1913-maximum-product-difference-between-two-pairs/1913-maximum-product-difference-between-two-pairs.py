class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        maxHeap = []
        minHeap = []

        for num in nums:
            if len(maxHeap) < 2:
                heapq.heappush(maxHeap, -num)
            else:
                if -maxHeap[0] > num:
                    heapq.heappop(maxHeap)
                    heapq.heappush(maxHeap, -num)
            
            if len(minHeap) < 2:
                heapq.heappush(minHeap, num)
            else:
                if minHeap[0] < num:
                    heapq.heappop(minHeap)
                    heapq.heappush(minHeap, num)

        maxP = minHeap[0] * minHeap[1]

        minP = -maxHeap[0] * -maxHeap[1]

        return maxP - minP
