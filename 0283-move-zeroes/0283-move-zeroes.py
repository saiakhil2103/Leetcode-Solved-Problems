class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        scanned = []
        n = len(nums)
        for num in nums:
            if num != 0:
                scanned.append(num)
        m = len(scanned)
        for i in range(m):
            nums[i] = scanned[i]
        for i in range(m, n):
            nums[i] = 0