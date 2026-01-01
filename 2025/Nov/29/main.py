from typing import  List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        sum = 0 
        for i in range(len(nums)):
            sum+=nums[i]
        mod = sum%k
        return mod
    
solution = Solution()
nums = [3,9,7]
k = 5
print(solution.minOperations(nums,k))