from typing import List

class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        prevLen = 0
        start = 0
        k = 0
        for i in range(1, len(nums) + 1):
            if i == len(nums) or nums[i] <= nums[i - 1]:
                length = i - start
                k = max(k, length // 2, min(prevLen, length))
                prevLen = length
                start = i
        return k
    
solution = Solution()
nums = [2,5,7,8,9,2,3,4,3,1]
print(solution.maxIncreasingSubarrays(nums)) 