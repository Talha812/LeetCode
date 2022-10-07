class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:                 
        
        
        record = [False]*(len(s)+1)
        record[0] = True

        for i in range(1, len(s)+1):
            for j in range(i):
                if record[j] and s[j:i] in wordDict:
                    record[i] = True
                    break
            #print(record)
            
        return record[-1]