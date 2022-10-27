class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1 += nums2
        nums1.sort()
        
        idx = len(nums1) // 2
        
        if len(nums1) % 2 == 0:
            return (nums1[idx] + nums1[idx - 1]) / 2
        else:
            return nums1[idx]