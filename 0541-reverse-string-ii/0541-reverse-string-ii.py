class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        count=len(s)//k
        ptr=0
        result=""
        def reverse(result, start, end):
            result=""
            for i in range(end,start-1,-1):
                result+=s[i]
            print(result)
            return result
        while ptr<len(s):
            print(ptr, ptr+k)
            if ptr+k<len(s):
                result+=reverse(result, ptr, ptr+k-1)
            else:
                result+=reverse(result, ptr, len(s)-1)
            if ptr+2*k<len(s):
                result+=s[ptr+k:ptr+2*k]
            else:
                result+=s[ptr+k:]
            ptr=2*k+ptr
        return result
