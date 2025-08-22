class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        min_i,max_i,min_j,max_j=-1,-1,-1,-1
        m,n=len(grid),len(grid[0])
        for j in range(n):
            for i in range(m):
                if grid[i][j]==1:
                    if min_i==-1:
                        min_i=j
                    if j>max_i:
                        max_i=j
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    if min_j==-1:
                        min_j=i
                    if i>max_j:
                        max_j=i
        print(min_i,min_j,max_i,max_j)
        return (max_i-min_i+1)*(max_j-min_j+1)