class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        ret=[]
        if len(nums1)>=len(nums2):
            long = nums1
            short = nums2
        else:
            long = nums2
            short = nums1
        
        for i in short:
            if i in long:
                ret.append(i)
                long.remove(i)
        return ret