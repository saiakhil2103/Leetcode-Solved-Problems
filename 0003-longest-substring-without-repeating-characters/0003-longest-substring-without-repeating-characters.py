class Solution:
    def lengthOfLongestSubstring(self, s):
        char_set = set()
        left = 0 
        answer = 0
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1 
            char_set.add(s[right])
            answer = max(answer, right - left + 1) 
        return answer 