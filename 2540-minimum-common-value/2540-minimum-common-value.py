class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        
        if len(nums1) < len(nums2):
            nums2 = set(nums2)
            for n in nums1:
                if n in nums2:
                    return n
        else:
            nums1 = set(nums1)
            for n in nums2:
                if n in nums1:
                    return n
        
        return -1