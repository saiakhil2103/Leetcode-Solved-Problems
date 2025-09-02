from collections import deque 

class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = "".join(ch.lower() for ch in s if ch.isalnum())
        def helper(left, right):
            if left >= right:
                return True 
            if cleaned[left] != cleaned[right]:
                return False
            return helper(left+1, right-1)
        return helper(0, len(cleaned)-1)