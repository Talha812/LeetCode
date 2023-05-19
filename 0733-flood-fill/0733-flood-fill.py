class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        def fill(image, sr, sc, newColor, str_pixel):
            if sr < 0 or sr > len(image)-1 or sc < 0 or sc > len(image[0])-1 or image[sr][sc] == newColor or image[sr][sc] != start_pixel:
                return
            
            image[sr][sc] = newColor
            fill(image, sr + 1, sc, newColor, start_pixel)
            fill(image, sr - 1, sc, newColor, start_pixel)
            fill(image, sr, sc + 1, newColor, start_pixel)
            fill(image, sr, sc - 1, newColor, start_pixel)
            
        
        newColor = color
        start_pixel = image[sr][sc]
        fill(image, sr, sc, newColor, start_pixel)
        
        return image