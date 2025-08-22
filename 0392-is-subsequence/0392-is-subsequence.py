class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ptr1,ptr2=0,0
        if s=="":
            return True
        m,n=len(s),len(t)
        while ptr1<m and ptr2<n:
            while ptr2<n and t[ptr2]!=s[ptr1]:
                ptr2+=1
            ptr1+=1
            ptr2+=1
        if ptr1==m and ptr2<=n:
            return True
        return False