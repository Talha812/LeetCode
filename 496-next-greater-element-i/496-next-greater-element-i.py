class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        
        ans = []
        
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if(nums1[i] == nums2[j]):
                    if(j<len(nums2)-1 and nums2[j+1] > nums2[j]):
                        ans.append(nums2[j+1])
                    else:
                        for k in range(j+2,len(nums2)):
                            if(nums2[k] > nums2[j]):
                                ans.append(nums2[k])
                                break
                        
                        else:
                            ans.append(-1)
        
        return ans