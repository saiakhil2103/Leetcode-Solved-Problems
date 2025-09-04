class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        visited = set()
        result = 0
        while fast != len(nums):
            if nums[fast] not in visited:
                visited.add(nums[fast])
                nums[slow] = nums[fast]
                slow += 1
                result += 1
            fast += 1
        return result