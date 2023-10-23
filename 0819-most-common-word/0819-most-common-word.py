class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        symbols = "!?',;. "
        
        # para_split = paragraph.replace("").split(" ")
        
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
        # for word in para_split:
        #     if word[-1] in symbols:
        #         if word[0: len(word)-1] in dic:
        #             dic[word[0: len(word)-1].lower()] += 1
        #         else:
        #             dic[word[0: len(word)-1].lower()] = 1
        #     else:
        #         if word.lower() in dic:
        #             dic[word.lower()] += 1
        #         else:
        #             dic[word.lower()] = 1
                    
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
    
    
            