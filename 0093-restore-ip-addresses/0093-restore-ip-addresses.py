class Solution:
    def valid(self, s, start, length):
        return length == 1 or (s[start] != '0' and (length < 3 or s[start:start+length] <= "255"))

    def restoreIpAddresses(self, s):
        def backtrack(start, path):
            if start == len(s) and len(path) == 4:
                ans.append(".".join(path))
                return
            
            for length in range(1, 4):
                if start + length > len(s):
                    break
                
                if self.valid(s, start, length):
                    backtrack(start + length, path + [s[start:start+length]])
        
        ans = []
        backtrack(0, [])
        return ans


