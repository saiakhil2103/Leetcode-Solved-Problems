class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n=len(nums)
        nums.sort()
        count=0
        for i in range(n-2):
            for j in range(i+1, n-1):
                target=nums[i]+nums[j]
                left,right=j+1,n-1
                pos=j
                while left<=right:
                    mid=(left+right)//2
                    if nums[mid]<target:
                        pos=mid
                        left=mid+1
                    else:
                        right=mid-1
                count+=(pos-j)
        return count
               