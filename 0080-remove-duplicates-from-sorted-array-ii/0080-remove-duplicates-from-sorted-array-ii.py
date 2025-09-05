class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        d={}
        for num in nums:
            d[num] = d.get(num, 0)+1
        i=0
        visited = set()
        for num in nums:
            if num not in visited:
                visited.add(num)
                if d[num] == 1:
                    nums[i]=num
                    i+=1
                elif d[num] >= 2:
                    for _ in range(2):
                        nums[i]=num
                        i+=1
        return i
