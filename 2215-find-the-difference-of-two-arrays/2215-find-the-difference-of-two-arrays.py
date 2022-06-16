class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        
        ans = []
        
        distinct_num1 = []      #stores values which are not in nums2
        for val in nums1:
            if val not in nums2 and val not in distinct_num1:
                distinct_num1.append(val)
        
        ans.append(distinct_num1)
        
        distinct_num2 = []      #stores values which are not in nums1
        for val in nums2:
            if val not in nums1 and val not in distinct_num2:
                distinct_num2.append(val)
        
        ans.append(distinct_num2)
        
        return ans
        