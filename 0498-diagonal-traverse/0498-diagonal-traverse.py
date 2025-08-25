class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        i,j,m,n=0,0,len(mat),len(mat[0])
        result=[]
        while i<m and j<n:
            while i>=0 and j<n:
                if i==m:
                    break
                print(i,j,"first")
                result.append(mat[i][j])
                i-=1
                j+=1
                
            if i<0 and j>=n:
                i+=2
                j-=1
            elif i>=0 and j>=n:
                i+=2
                j-=1
            elif i<0:
                i+=1
            while j>=0 and i<m:
                if j==n:
                    break
                print(i,j,"second")
                result.append(mat[i][j])
                i+=1
                j-=1
                
            if i>=m:
                j+=2
                i-=1
            elif j<0:
                j+=1
        return result 
