class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        for i in range(0, len(nums), 2):
            min_idx = i
            for j in range(i+2, len(nums), 2):
                if nums[min_idx] > nums[j]:
                    min_idx = j
            nums[i], nums[min_idx] = nums[min_idx], nums[i]
        
        for i in range(1, len(nums), 2):
            max_idx = i
            for j in range(i+2, len(nums), 2):
                if nums[max_idx] < nums[j]:
                    max_idx = j
            nums[i], nums[max_idx] = nums[max_idx], nums[i]           
        return nums