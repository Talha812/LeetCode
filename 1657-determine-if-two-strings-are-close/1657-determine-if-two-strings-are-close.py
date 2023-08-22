class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        if len(word1) != len(word2):
            return False
        dic1 = {}
        dic2 = {}
        for i in range(len(word1)):
            if word1[i] not in dic1:
                dic1[word1[i]] = 1
            else:
                dic1[word1[i]] += 1
                
            if word2[i] not in dic2:
                dic2[word2[i]] = 1
            else:
                dic2[word2[i]] += 1
        
        w1_keys = set(dic1.keys())
        w2_keys = set(dic2.keys())
        
        w1_values = dic1.values()
        w2_values = dic2.values()
        
        
        w1_values_count = Counter(w1_values)
        w2_values_count = Counter(w2_values)
        
        
        return w1_keys == w2_keys and w1_values_count == w2_values_count
        