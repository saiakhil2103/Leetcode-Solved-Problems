class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        result=0
        m,n=len(mat),len(mat[0])
        dp=[[0 for _ in range(n)] for _ in range(m)]
        heights=[[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if mat[i][j]==1:
                    heights[i][j]=1+heights[i-1][j]
        for i in range(m):
            for j in range(n):
                if mat[i][j]==1:
                    s=0
                    h=heights[i][j]
                    for k in range(j,-1,-1):
                        h=min(heights[i][k], h)
                        s+=h
                    result+=s
        return result


