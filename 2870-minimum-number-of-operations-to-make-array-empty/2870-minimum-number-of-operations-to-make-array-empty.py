class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        dic = {}
        for n in nums:
            if n in dic:
                dic[n] += 1
            else:
                dic[n] = 1
                
        if min(dic.values()) == 1:
            return -1
        
        opr = 0
        for num, count in dic.items():
            opr += ceil(count/3)
            
        return opr