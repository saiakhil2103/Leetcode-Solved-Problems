class Solution:
    def validPalindrome(self, s: str) -> bool:
        left,right=0,len(s)-1
        def isPalindrome(s):
            return s==s[::-1]
        while left<=right:
            if s[left]==s[right]:
                left+=1
                right-=1
            else:
                break
        print(left, right)
        if left>right:
            return True
        # print(s[left+1:right+1], s[left:right])
        return isPalindrome(s[left+1:right+1]) or isPalindrome(s[left:right])