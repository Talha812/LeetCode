class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        def fill(image, sr, sc, newColor, start):
            if sr < 0 or sr > len(image)-1 or sc < 0 or sc > len(image[0])-1 or image[sr][sc] == newColor or image[sr][sc] != start:
                return
            
            image[sr][sc] = newColor
            fill(image, sr + 1, sc, newColor, start)
            fill(image, sr - 1, sc, newColor, start)
            fill(image, sr, sc + 1, newColor, start)
            fill(image, sr, sc - 1, newColor, start)
            
        
        newColor = color
        start = image[sr][sc]
        fill(image, sr, sc, newColor, start)
        
        return image