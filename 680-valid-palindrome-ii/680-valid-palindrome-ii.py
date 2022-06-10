class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(self, s, start, end):
            while(start<end):
                if(s[start] != s[end]):
                    return False
                start += 1
                end -= 1
            return True
        
        start = 0
        end = len(s)-1
        while(start < end):
            if(s[start] != s[end]):
                return isPalindrome(self, s, start, end-1) or isPalindrome(self, s, start+1, end)
            start += 1
            end -= 1
        
        return True