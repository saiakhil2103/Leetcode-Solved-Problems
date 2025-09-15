class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split()
        count = 0 
        for word in words:
            is_found = False
            for letter in brokenLetters:
                if letter in word:
                    is_found = True
                    break
            if not is_found:
                count += 1
        return count 