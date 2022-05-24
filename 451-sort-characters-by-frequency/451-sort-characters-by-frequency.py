class Solution:
    def frequencySort(self, s: str) -> str:
        
        dic = {}
        
        for i in range(len(s)):
            if(s[i] in dic):
                dic[s[i]] += 1
            else:
                dic[s[i]] = 1
        
        count_list = list(dic.values())
        count_list.sort(reverse = True)
        
        
        ans = ""
        
        index = 0
        
        while(index<len(count_list)):
            for i in dic.keys():
                if i not in ans and dic.get(i) == count_list[index]:
                    for put in range(count_list[index]):
                        ans += i
            
            index += 1
        
        return ans
    
    