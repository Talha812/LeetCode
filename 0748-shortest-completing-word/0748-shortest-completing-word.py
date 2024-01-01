class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        
        dic = {}
        for ch in licensePlate:
            if ch in "0123456789" or ch == " ":
                continue
            
            if ch.lower() in dic:
                dic[ch.lower()] += 1
            else:
                dic[ch.lower()] = 1
        
        ans = ""
        for word in words:
            count = Counter(word)
            
            flag = True
            for k, v in dic.items():
                if k in count and count[k] >= v:
                    continue
                else:
                    flag = False
                    break
            
            if flag:
                if ans == "" or len(ans) > len(word):
                    ans = word
        
        return ans