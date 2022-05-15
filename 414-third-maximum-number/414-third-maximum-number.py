class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        
        maxi = []
        count = 0
        nums.sort(reverse = True)
        
        for i in nums:
            if i not in maxi and count<3:
                maxi.append(i)
                count += 1
                
            if i in maxi:
                continue
                
        if count == 3:
            return maxi[-1] 
        else:
            return max(maxi)