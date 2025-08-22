class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result=list(set([i for i in nums1 if i in nums2]))
        return result