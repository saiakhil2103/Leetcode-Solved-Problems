class Solution:
    def sortColors(self, nums: List[int]) -> None:
        zeros_count = 0
        ones_count = 0 
        twos_count = 0 
        for num in nums:
            if num == 0:
                zeros_count += 1
            elif num == 1:
                ones_count += 1
            else:
                twos_count += 1
        i = 0
        while i < zeros_count:
            nums[i] = 0 
            i += 1
        while i < zeros_count + ones_count:
            nums[i] = 1 
            i += 1
        while i < len(nums):
            nums[i] = 2
            i += 1