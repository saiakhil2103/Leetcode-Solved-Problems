class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result=set()
        m,n=len(nums1),len(nums2)
        nums1.sort()
        nums2.sort()
        ptr1=0
        ptr2=0
        while ptr1<m and ptr2<n:
            if nums1[ptr1]==nums2[ptr2] and nums1[ptr1] not in result:
                result.add(nums1[ptr1])
            elif nums1[ptr1]>nums2[ptr2]:
                ptr2+=1
            else:
                ptr1+=1
        return list(result)
