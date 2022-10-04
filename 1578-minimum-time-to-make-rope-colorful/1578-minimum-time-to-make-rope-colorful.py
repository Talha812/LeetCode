class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        
        dic = {}
        
        for i in range(len(colors)):
            if dic.get(colors[i]) != None:
                dic.get(colors[i]).append(i)
            else:
                dic[colors[i]] = [i]
        
        #print(dic)
        ans = 0
        for val in dic.values():
            for i in range(1,len(val)):
                if(val[i-1]+1 == val[i]):
                    ans += min(neededTime[val[i-1]], neededTime[val[i]])
                    if(neededTime[val[i]] < neededTime[val[i-1]]):
                        neededTime[val[i]] = neededTime[val[i-1]]
        
        return ans
                    
        