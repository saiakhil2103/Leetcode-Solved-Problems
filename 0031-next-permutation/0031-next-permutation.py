class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        ind = -1
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                ind = i 
                break 
        if ind == -1:
            nums[::] = nums[::-1]
            return 
        for i in range(n-1, ind, -1):
            if nums[i] > nums[ind]:
                nums[i], nums[ind] = nums[ind], nums[i] 
                break 
        nums[ind+1: ] = nums[ind+1: ][::-1]
