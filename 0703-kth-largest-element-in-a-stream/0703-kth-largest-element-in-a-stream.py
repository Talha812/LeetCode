class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.size = k
        self.minHeap = []
        for n in nums:
            heappush(self.minHeap, n)
            if len(self.minHeap) > self.size:
                heappop(self.minHeap)
        

    def add(self, val: int) -> int:
        heappush(self.minHeap, val)
        if len(self.minHeap) > self.size:
            heappop(self.minHeap)
        
        return self.minHeap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)