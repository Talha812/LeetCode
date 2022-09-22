class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        
        copy = sorted(arr.copy())
        
        rank  = [1]*len(copy)
        val = 1
        for i in range(1,len(copy)):
            if(copy[i] > copy[i-1]):
                rank[i] = val+1
                val += 1
            else:
                rank[i] = val
        
        #print(rank)
        
        dic = {}
        for i in range(len(copy)):
            if(dic.get(copy[i]) == None):
                dic[copy[i]] = rank[i]
        
        
        ans = [0]*len(copy)
        
        for i in range(len(arr)):
            ans[i] = dic[arr[i]]
        
        return ans
        