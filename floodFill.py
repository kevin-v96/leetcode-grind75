#https://leetcode.com/problems/flood-fill/
class Solution:
    def fill(self, image, sr, sc, color, currentColor):
        if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]):
            return
        
        if currentColor != image[sr][sc]:
            return

        image[sr][sc] = color

        self.fill(image, sr - 1, sc, color, currentColor)
        self.fill(image, sr, sc - 1, color, currentColor)
        self.fill(image, sr + 1, sc, color, currentColor)
        self.fill(image, sr, sc + 1, color, currentColor)

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image

        self.fill(image, sr, sc, color, image[sr][sc])

        return image