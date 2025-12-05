from typing import List

class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        total = sum(nums)
        left = 0
        ans = 0
        for i in range(len(nums) - 1):
            left += nums[i]
            right = total - left
            if (left - right) % 2 == 0:
                ans += 1
        return ans
    

solution = Solution()
nums = [10,10,3,7,6]
print(solution.countPartitions(nums))