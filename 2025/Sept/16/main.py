from math import gcd
from typing import List

class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = []
        for num in nums:
            curr = num
            while stack:
                g = gcd(stack[-1], curr)
                if g == 1:
                    break
                curr = stack[-1] * curr // g
                stack.pop()
            stack.append(curr)
        return stack

solution = Solution()
nums = [6,4,3,2,7,6,2]
print(solution.replaceNonCoprimes(nums))