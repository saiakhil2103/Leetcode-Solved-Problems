class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_count = {}
        answer = 0 
        curr_sum = 0 
        prefix_count[0] = 1
        for i in range(len(nums)):
            curr_sum += nums[i]
            answer += prefix_count.get(curr_sum - k, 0)
            prefix_count[curr_sum] = prefix_count.get(curr_sum, 0) + 1 
        return answer