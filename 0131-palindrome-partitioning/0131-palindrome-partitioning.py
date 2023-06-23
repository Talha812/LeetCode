class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def checkPalindrome(s, start, end):
            
            while start < end:
                if s[start] != s[end]:
                    return False
                
                start += 1
                end -= 1
            
            return True
        
        
        ans = []
        
        def dfs(s, path, start, ans):
            if start >= len(s):
                ans.append(path.copy())
                return
                
            for i in range(start, len(s)):
                if checkPalindrome(s, start, i):
                    path.append(s[start : i+1])
                    dfs(s, path, i + 1, ans)
                    path.pop()
            
            return ans
        
        return dfs(s, [], 0, ans)
