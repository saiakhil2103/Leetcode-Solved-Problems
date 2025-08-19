class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        answer=0
        consecutive_zeros=0
        for index, value in enumerate(nums):
            if value==0:
                i=index-1
                answer+=consecutive_zeros+1
                consecutive_zeros+=1
            else:
                consecutive_zeros=0
        return answer