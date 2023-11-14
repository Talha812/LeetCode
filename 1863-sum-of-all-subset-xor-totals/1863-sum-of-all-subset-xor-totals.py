class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def calculateXOR(arr):
            if len(arr) == 0:
                return 0
            elif len(arr) == 1:
                return arr[0]
            else:
                ans = 0
                for n in arr:
                    ans = ans^n
                return ans
        
        global output
        output = 0
        
        def subsets(index, path):
            global output
            if len(path) >= 0:
                output += calculateXOR(path)
            
            for i in range(index, len(nums)):
                subsets(i+1, path + [nums[i]])
        
        subsets(0, [])
        
        return output