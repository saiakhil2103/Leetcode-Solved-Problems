class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_s = "".join(ch.lower() for ch in s if ch.isalnum())
        return cleaned_s == cleaned_s[::-1]