class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        symbols = "!?',;. "        
        dic = {}
        i = 0
        while i < len(paragraph):
            buffer = ""
            while i < len(paragraph) and paragraph[i] not in symbols:
                buffer += paragraph[i]
                i += 1
            #print("Buffer : ", buffer)
            if buffer.lower() not in banned and buffer != "":
                if buffer.lower() in dic:
                    dic[buffer.lower()] += 1
                else:
                    dic[buffer.lower()] = 1
            
            i += 1
                    
        most_freq = -1
        ans = ""
        
        for key, val in dic.items():
            if key in banned:
                continue
            else:
                if val > most_freq:
                    most_freq = val
                    ans = key
                    
        return ans.lower()
    
    
            