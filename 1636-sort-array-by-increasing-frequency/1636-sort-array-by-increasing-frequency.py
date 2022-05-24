class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        
        dic = {}
        
        #putting values against the count
        for i in nums:
            if nums.count(i) in dic:
                dic[nums.count(i)].append(i)
            else:
                dic[nums.count(i)] = [i]
        
        for i in dic.values():
            i.sort()
        
        # print(dic)
        
        print(dic)
        
        ans = []
        for i in sorted(dic.keys()):
            if len(dic[i]) == 1:
                ans.append(dic[i][0])
            else:
                for val in range(len(list(dic[i]))-1, -1, -1):
                    if dic[i][val] not in ans:
                        for put in range(i):
                            ans.append(dic[i][val])
                            
        return ans
                
        
        
        