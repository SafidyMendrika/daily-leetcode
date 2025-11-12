from math import gcd

class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)
        ones = nums.count(1)
        if ones:
            return n - ones
        best = float('inf')
        for i in range(n):
            g = nums[i]
            for j in range(i+1, n):
                g = gcd(g, nums[j])
                if g == 1:
                    best = min(best, j - i + 1)
                    break
        return -1 if best == float('inf') else best+n-2
    
solution = Solution()
nums = [2,6,3,4]
print(solution.minOperations(nums))