class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    total_sum = nums[i]+nums[j]+nums[k]
                    left, right = k+1, n-1
                    while left<=right:
                        mid=(left+right)//2
                        if nums[mid] == target-total_sum:
                            temp = [nums[i], nums[j], nums[k], target-total_sum] 
                            result.append(temp)
                            break
                        elif nums[mid] > target-total_sum:
                            right = mid - 1
                        else:
                            left = mid + 1
        updated_result = []
        for res in result:
            if sorted(res) not in updated_result:
                updated_result.append(sorted(res))
        return updated_result
