class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        
        lst = s.split(" ")
        prev = -1
        for string in lst:
            if ord(string[0]) >= 97 and ord(string[0]) <= 122:
                continue
            else:
                if int(string) <= prev:
                    return False
                
                prev = int(string)
        
        return True