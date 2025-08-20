class Solution:
    def reverseVowels(self, s: str) -> str:
        start=0
        end=len(s)-1
        s=list(s)
        while start<end:
            while start<end and s[start] not in "AEIOUaeiou":
                start+=1
            while start<end and s[end] not in "AEIOUaeiou":
                end-=1
            s[start],s[end]=s[end],s[start]
            start+=1
            end-=1
        s="".join(s)
        return s

        