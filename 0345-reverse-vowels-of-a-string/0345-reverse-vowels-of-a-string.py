class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = []
        for ch in s:
            if ch in "aeiouAEIOU":
                vowels.append(ch)
        l = list(s)
        for index, value in enumerate(l):
            if value in "aeiouAEIOU":
                l[index] = vowels.pop()
        return "".join(l)