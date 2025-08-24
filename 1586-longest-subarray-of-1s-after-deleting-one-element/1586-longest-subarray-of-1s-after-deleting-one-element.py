class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if sum(nums)==len(nums):
            return len(nums)-1
        if sum(nums)==0:
            return 0
        lsum=[]
        rsum=[0 for _ in range(len(nums))]
        for i in range(len(nums)):
            if nums[i]==0:
                lsum.append(0)
            else:
                lsum.append(1+(lsum[-1] if i!=0 else 0))
        for i in range(len(nums)-1, -1, -1):
            if nums[i]==0:
                rsum[i]=0
            else:
                rsum[i]=(1+(rsum[i+1] if i!=len(nums)-1 else 0))
        answer=0
        print(lsum, rsum)
        for i in range(len(nums)):
            if nums[i]==0:
                if i!=0 and i!=len(nums)-1:
                    print(i)
                    answer=max(answer, lsum[i-1]+rsum[i+1])
                elif i==0:
                    answer=max(answer, rsum[1])
                else:
                    answer=max(answer, lsum[-2])
        return answer
                