class Solution:
    def reverseVowels(self, s: str) -> str:
        chars = list(s)
        def helper(left, right):
            if left >= right:
                return True 
            if left < right and s[left] not in "aeiouAEIOU":
                helper(left+1, right)
            elif left < right and s[right] not in "aeiouAEIOU":
                helper(left, right-1)
            else:
                chars[left], chars[right] = chars[right], chars[left]
                helper(left+1, right-1)
        helper(0, len(s)-1)
        return "".join(chars)