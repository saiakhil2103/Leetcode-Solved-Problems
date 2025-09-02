class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        result = 0
        diff = float('inf')
        for i in range(n):
            left = i + 1
            right = n - 1
            while left < right:
                total = nums[left] + nums[right] + nums[i]
                curr_diff = abs(target - total)
                if curr_diff < diff:
                    diff = curr_diff 
                    result = total 
                if total < target:
                    left += 1
                else:
                    right -= 1
        return result

