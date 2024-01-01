class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:

        minHeap = []
        result = []

        for i in range(min(k, len(nums1))):
            heapq.heappush(minHeap, (nums1[i] + nums2[0], i, 0))

        while minHeap and len(result) < k:
            smallestSum, index1, index2 = heapq.heappop(minHeap)
            result.append([nums1[index1], nums2[index2]])

            if index2 + 1 < len(nums2):
                heapq.heappush(minHeap, (nums1[index1] + nums2[index2 + 1], index1, index2 + 1))

        return result