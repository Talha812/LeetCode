class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        if len(nums) == 0:
            return []
        
        ans = []
        temp = [nums[0]]
        i = 1
        while i < len(nums):
            if nums[i] == nums[i-1] + 1:
                temp.append(nums[i])
                i += 1
                continue
            elif nums[i] != nums[i-1] + 1:  
                if len(temp) == 1:
                    ans.append(str(temp[0]))
                    temp = [nums[i]]
                    i += 1
                else:
                    ans.append(str(temp[0]) + "->" + str(temp[-1]))
                    temp = [nums[i]]
                    i += 1  
        if temp:
            if len(temp) == 1:
                ans.append(str(temp[0]))
            else:
                ans.append(str(temp[0]) + "->" + str(temp[-1]))
                
        return ans
        
        