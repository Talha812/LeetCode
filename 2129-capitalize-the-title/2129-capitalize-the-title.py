class Solution:
    def capitalizeTitle(self, title: str) -> str:
        
        words = title.split(" ")
        
        ans = ""
        for i in range(len(words)):
            if i == len(words)-1:
                if len(words[i]) > 2:
                    ans += words[i][0].upper() + words[i][1:].lower()
                else:
                    ans += words[i].lower()
            else:
                if len(words[i]) > 2:
                    ans += words[i][0].upper() + words[i][1:].lower() + " "
                else:
                    ans += words[i].lower() + " "
        
        return ans