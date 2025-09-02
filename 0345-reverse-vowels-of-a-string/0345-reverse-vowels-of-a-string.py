class Solution:
    def reverseVowels(self, s: str) -> str:
        left, right = 0, len(s)-1
        s = list(s)
        while left < right:
            while left < right and s[left] not in "AEIOUaeiou":
                left += 1
            while left < right and s[right] not in "AEIOUaeiou":
                right -= 1
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return "".join(s)
