class Solution:
    def reverseWords(self, s: str) -> str:
        
        def split_S(self, s):
            ans = []
            s += " "
            word = ""
            for i in range(len(s)):
                if(s[i] == " "):
                    ans.append(word)
                    word = ""
                else:
                    word += s[i]
            
            return ans
        
        splitted = split_S(self, s)
        ans = []
        for word in splitted:
            
            arr_word = []
            for ch in word:
                arr_word.append(ch)
            
            i = 0
            j = len(arr_word)-1
            
            while(i<j):
                arr_word[i], arr_word[j] = arr_word[j], arr_word[i]
                i += 1
                j -= 1
                
            ans.append("".join(arr_word))
                
        return " ".join(ans)