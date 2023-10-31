class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
            
        visited = set()
        i = 1
        friend = 1
        while True:
            if friend in visited or len(visited) == n:
                break
            visited.add(friend)
            friend += (i * k)
            friend = (friend - 1) % n + 1
            i += 1
        ans = []
        for f in range(1, n+1):
            if f not in visited:
                ans.append(f)
        return ans