class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        answer = 0 
        min_counts = []
        summ = 0 
        for num in nums:
            summ += num
            min_counts.append(summ)
        min_value = min(min_counts)
        if min_value > 0:
            return 1 
        return abs(min_value) + 1