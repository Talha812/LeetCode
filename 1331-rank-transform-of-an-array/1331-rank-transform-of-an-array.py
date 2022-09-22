class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        
        copy = sorted(arr.copy())
        
        rank  = [1]*len(copy)
        ind = 1
        val = 1
        for i in range(1,len(copy)):
            if(copy[i] > copy[i-1]):
                rank[ind] = val+1
                ind += 1
                val += 1
            else:
                rank[ind] = val
                ind += 1
        
        #print(rank)
        
        dic = {}
        for i in range(len(copy)):
            if copy[i] not in dic:
                dic[copy[i]] = rank[i]
                
        ans = [0]*len(copy)
        
        for i in range(len(arr)):
            ans[i] = dic[arr[i]]
        
        return ans
        