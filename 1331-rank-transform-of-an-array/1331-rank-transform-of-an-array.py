class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        
        if(arr == []):
            return []
        
        copy = sorted(arr.copy())
        
        rank  = [1]*len(copy)
        val = 1
        dic = {copy[0]: 1}
        for i in range(1,len(copy)):
            if(copy[i] > copy[i-1]):
                rank[i] = val+1
                val += 1
                if(dic.get(copy[i]) == None):
                    dic[copy[i]] = rank[i]
            else:
                rank[i] = val
        
        #print(rank)
        
        ans = [0]*len(copy)
        
        for i in range(len(arr)):
            ans[i] = dic[arr[i]]
        
        return ans
        
        
        # 1 -> log(n) -> n -> nlog(n) -> n^2 -> 2^n -> n!