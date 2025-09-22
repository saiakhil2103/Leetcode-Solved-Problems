class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        max_freq = max(freq.values())
        count = 0
        for value in freq.values():
            if value == max_freq:
                count += value
        return count