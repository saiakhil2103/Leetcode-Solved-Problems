class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        left, right = 0, 0
        freq = {}
        answer = 0 
        while right < n:
            freq[s[right]] = freq.get(s[right], 0) + 1
            if freq[s[right]] == 1:
                answer = max(answer, right-left+1)
            else:
                while freq[s[right]] != 1:
                    freq[s[left]] -= 1
                    left += 1
            right += 1
        return answer

