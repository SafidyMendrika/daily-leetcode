from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        total = 0

        i = 0
        while(i < len(nums)):

            if(nums[i] % 3 != 0):
                
                lower_limit = nums[i] - (nums[i] % 3)
                upper_limit = lower_limit + 3

                difference1 = nums[i] - lower_limit
                difference2 = upper_limit - nums[i]

                if(difference1 < difference2):
                    total += difference1
                else:
                    total += difference2

            i += 1

        return total
    
solution = Solution()
nums = [1,2,3,4]
print(solution.minimumOperations(nums))