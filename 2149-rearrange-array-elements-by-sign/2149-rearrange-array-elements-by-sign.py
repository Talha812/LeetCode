class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        pos = []
        neg = []
        
        for i in nums:
            if(i<0):
                neg.append(i)
            else:
                pos.append(i)
        
        ans = []
        p = 0
        n = 0
        for i in range(len(nums)):
            if(i%2 == 0):
                ans.append(pos[p])
                p += 1
            else:
                ans.append(neg[n])
                n += 1
        
        return ans