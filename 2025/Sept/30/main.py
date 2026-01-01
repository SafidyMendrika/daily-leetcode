from typing import List

class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        size = len(nums)
        while(size > 1):
            for i in range(len(nums)-1):
                nums[i] = (nums[i] + nums[i+1]) % 10
            size-=1
            

        return nums[0]
    
solution = Solution()
nums = [1,2,3,4,5]
print(solution.triangularSum(nums))