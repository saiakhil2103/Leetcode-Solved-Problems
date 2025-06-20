class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i, j = 0, 0
        m, n = len(matrix), len(matrix[0])
        found = False
        while not found:
            if matrix[i][j] == target:
                found = True 
                break
            elif i+1 < m and matrix[i+1][j] <= target:
                i = i + 1
            elif j+1 < n and matrix[i][j+1] <= target:
                j = j + 1
            else:
                found = False
                break 
        return found