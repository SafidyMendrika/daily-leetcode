from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        stack = []
        ans = 0
        for num in nums:
            while stack and stack[-1] > num:
                stack.pop()
            if num == 0:
                continue
            if not stack or stack[-1] < num:
                ans += 1
                stack.append(num)
        return ans
    
solution = Solution()
nums = [1,2,1,2,1,2]
print(solution.minOperations(nums))