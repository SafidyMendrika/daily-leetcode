from typing import List

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        count = 0
        if n <= 2:
            return 0
            
        for k in range(2, n):
            i = 0
            j = k - 1
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    count += j - i
                    j -= 1
                else:
                    i += 1
        return count
    
solution = Solution()
nums = [2,2,3,4]
print(solution.triangleNumber(nums))  