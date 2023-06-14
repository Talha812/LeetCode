class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        products.sort()
        
        def getProducts(products, keyStrokes):
            
            words = []
            
            for p in products:
                if len(p) >= len(keyStrokes) and p[0:len(keyStrokes)] == keyStrokes:
                    words.append(p)
                
                if len(words) == 3:
                    break
            
            return words
        
        buffer = ""
        ans = []
        i = 0
        while i < len(searchWord):
            buffer += searchWord[i]
            words = getProducts(products, buffer)
                
            ans.append(words)
            i += 1
        
        return ans
        