from typing import List

class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        total_sum = sum(nums)
        left_sum = 0
        right_sum = total_sum
        
        for i in range(n):
            if nums[i] == 0:
                if 0 <= left_sum - right_sum <= 1:
                    ans += 1
                if 0 <= right_sum - left_sum <= 1:
                    ans += 1
            else:
                left_sum += nums[i]
                right_sum -= nums[i]
        
        return ans
    
solution = Solution()
nums = [1,0,2,0,3]
print(solution.countValidSelections(nums)) 