#https://leetcode.com/problems/01-matrix/
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        if rows == 0:
            return []
        cols = len(mat[0])
        mx = rows * cols
        distance = [[mx for _ in range(cols)] for _ in range(rows)]

        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, -1, -1):
                if mat[i][j] == 0:
                    distance[i][j] = 0
                else:
                    #we do a backwards pass first
                    right = distance[i][j + 1] if j + 1 < cols else mx
                    down = distance[i + 1][j] if i + 1 < rows else mx
                    distance[i][j] = 1 + min(right, down)

        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    distance[i][j] = 0
                else:
                    #we do a forward pass and select the previous distance or the 
                    left = distance[i][j - 1] if j - 1 >= 0 else mx
                    top = distance[i - 1][j] if i - 1 >= 0 else mx
                    distance[i][j] = min(distance[i][j], 1 + min(left, top))

        return distance