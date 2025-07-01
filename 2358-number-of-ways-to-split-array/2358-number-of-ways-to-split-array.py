class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        prefix_sum = []
        sum1 = 0 
        for num in nums:
            sum1 += num 
            prefix_sum.append(sum1)
        postfix_sum = []
        total_sum = sum(nums)
        for num in nums:
            total_sum -= num 
            postfix_sum.append(total_sum)
        answer = 0 
        print(prefix_sum)
        print(postfix_sum)
        for i in range(len(nums)-1):
            if prefix_sum[i] >= postfix_sum[i]:
                answer += 1
        return answer
