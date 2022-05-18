# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        
        first = 1
        last = n
        
        while(first<=last):
            
            guessed_num = (first+last)//2
            
            if(guess(guessed_num) == 0):
                return guessed_num
            
            elif(guess(guessed_num) == 1):
                first = guessed_num + 1
            
            else:
                last = guessed_num - 1
            
            