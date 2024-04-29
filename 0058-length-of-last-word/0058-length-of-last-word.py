class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
    	# Approach 1
        arr = s.split()
        
        return len(arr[-1])
        
        # Approach 2
        c = 0
        # for i in s[::-1]:
        #     if i == " ":
        #         if c >= 1:
        #             return c
        #     else:
        #         c += 1
        # return c
                