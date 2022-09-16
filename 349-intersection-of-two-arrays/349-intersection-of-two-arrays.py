class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        intersaction = set()
        
        for i in nums1:
            for j in nums2:
                if(i==j):
                    intersaction.add(i)
                    
        return list(intersaction)