class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float('inf')
        left = 0
        curr_sum = 0
        for right in range(len(nums)):
            curr_sum += nums[right]
            while curr_sum >= target:
                if right-left+1 < min_len:
                    min_len = right-left+1
                curr_sum -= nums[left]
                left += 1
        return min_len if min_len != float('inf') else 0