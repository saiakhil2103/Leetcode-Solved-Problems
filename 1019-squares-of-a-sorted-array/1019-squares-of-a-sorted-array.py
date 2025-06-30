class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = [] 
        left, right = 0, -1
        i = 0 
        while i < len(nums):
            if nums[i] >= 0:
                right = i 
                break
            i += 1 
        left = right - 1 
        if left == -1:
            return [num ** 2 for num in nums]
        if right == -1:
            return [num ** 2 for num in nums][::-1]
        while left >= 0 and right < len(nums):
            if abs(nums[left]) > nums[right]:
                result.append(nums[right] ** 2)
                right += 1
            elif abs(nums[left]) <= nums[right]:
                result.append(nums[left] ** 2)
                left -= 1
        while left >= 0:
            result.append(nums[left] ** 2)
            left -= 1
        while right < len(nums):
            result.append(nums[right] ** 2)
            right += 1
        return result
