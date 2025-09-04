class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        result = []
        visited = set()
        i=0
        for num in nums:
            if num not in visited:
                result.append(num)
                visited.add(num)
        nums[:]=result