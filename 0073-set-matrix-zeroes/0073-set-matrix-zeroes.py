class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        zeros_positions = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zeros_positions.append([i, j])
        for x, y in zeros_positions:
            for i in range(m):
                matrix[i][y] = 0
            for i in range(n):
                matrix[x][i] = 0
