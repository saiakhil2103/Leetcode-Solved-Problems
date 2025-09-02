class Solution:
    def reverseVowels(self, s: str) -> str:
        stack = [ch for ch in s if ch in "aeiouAEIOU"]
        chars = [] 
        for ch in s:
            if ch in "aeiouAEIOU":
                chars.append(stack.pop())
            else:
                chars.append(ch)
        return "".join(chars)