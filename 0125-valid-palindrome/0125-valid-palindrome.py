class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""
        for c in s:
            if c.isalnum():
                new_s += c 
        print(new_s)
        return new_s.lower() == new_s[::-1].lower()