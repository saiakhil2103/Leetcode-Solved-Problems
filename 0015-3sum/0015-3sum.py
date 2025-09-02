from collections import Counter

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        freq = Counter(nums)
        unique_nums = sorted(freq.keys())
        res = []
        for index, a in enumerate(unique_nums):
            for j in range(index, len(unique_nums)):
                b = unique_nums[j]
                c = -(a+b)
                if c<b:
                    continue
                if c not in freq:
                    continue 
                if a == b == c:
                    if freq[a] >= 3:
                        res.append([a,b,c])
                elif a == b != c:
                    if freq[a] >= 2:
                        res.append([a,b,c])
                elif a != b and b == c:
                    if freq[b] >= 2:
                        res.append([a,b,c])
                elif a != b and b != c and a != c:
                    res.append([a,b,c])
        return res 
