class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        
        characters = ""
        
        for ch in s:
            if ch != "-":
                characters += ch
        
        ans = []
        i = len(characters)-1
        
        while i >= 0:
            buffer = ""
            c = 0
            while c < k and i >= 0:
                buffer = characters[i].upper() + buffer
                i -= 1
                c += 1
            
            ans.append(buffer)
        
        ans.reverse()
        
        return "-".join(ans)