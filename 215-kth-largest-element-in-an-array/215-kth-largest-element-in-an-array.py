class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        # Method 1 Quick Select T(Average): O(N), T(worse): O(N^2)
        k = len(nums) - k
        
        def quickSelect(l, r):
            pivot, p = nums[r], l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]
            
            if p > k:   return quickSelect(l, p-1)
            elif p < k: return quickSelect(p + 1, r)
            else:       return nums[p]
            
        return quickSelect(0, len(nums) - 1)
    
        
        
"""               
        # Method # 02 (Merge Sort) T: O(nlogn)
        def mergeSort(nums):
            if len(nums) > 1:
                mid = len(nums)//2
                
                L = nums[:mid]
                R = nums[mid:]
                
                mergeSort(L)
                mergeSort(R)
                
                i = j = k = 0
                while i < len(L) and j < len(R):
                    if L[i] < R[j]:
                        nums[k] = L[i]
                        i += 1
                    else:
                        nums[k] = R[j]
                        j += 1
                    k += 1
                while i < len(L):
                    nums[k] = L[i]
                    i += 1
                    k += 1
                while j < len(R):
                    nums[k] = R[j]
                    j += 1
                    k += 1
        mergeSort(nums)
            
        return nums[len(nums)-k]
        
"""