class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m - 1
        j = n - 1
        r = m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[r] = nums1[i]
                i -= 1
            else:
                nums1[r] = nums2[j]
                j -= 1
            r -= 1 
            print(nums1, i, j)
        while j >= 0:
            nums1[r] = nums2[j]
            r -= 1
            j -= 1
        