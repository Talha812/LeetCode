class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        
        concat = ""
        for i in words:
            concat += i
            if(s == concat):
                return True
        
        return False