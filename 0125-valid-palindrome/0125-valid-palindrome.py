class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_s = "".join(ch.lower() for ch in s if ch.isalnum())
        left, right = 0, len(cleaned_s)-1
        while left<=right:
            if cleaned_s[left] != cleaned_s[right]:
                return False
            left += 1
            right -= 1
        return True