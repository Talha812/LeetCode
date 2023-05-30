class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        
        distances = []

        for point in points:
            distances.append((pow(point[0]-0, 2)+ pow(point[1]-0, 2) , point))
        
        distances.sort(reverse = True)
        ans = []
        while k > 0:
            distance, point = distances.pop()
            ans.append(point)
            k -= 1

        return ans