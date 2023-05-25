class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        
        def isPalindrome(s):
            i = 0
            j = len(s) - 1
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            
            return True
        
        def getNumberWithBase(num, base):
            
            ans = ""
            
            while num > 0:
                rem = num % base
                ans = ans + str(rem)
                num = num // base
            
            return ans
        
        base = 2
        while base <= n-2:
            s = getNumberWithBase(n, base)
            checkPalindrome = isPalindrome(s)
            
            if not checkPalindrome:
                return False
            
            base += 1
        
        return True