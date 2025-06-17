class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        duplicate = [-1] * len(nums)
        for num in nums:
            if duplicate[num-1] == -1:
                duplicate[num-1] = 1 
            else:
                return num 
        
            
