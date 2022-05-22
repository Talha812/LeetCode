class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        
        dic = {}
        
        for i in candyType:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        
        types = len(dic.keys())
        
        if(types >= len(candyType)//2):
            return len(candyType)//2
        else:
            return types