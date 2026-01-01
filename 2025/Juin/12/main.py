class Solution:
    def maxAdjacentDistance(self, nums: list[int]) -> int:
        ans = 0
        for i in range(1, len(nums)):
            ans = max(ans, abs(nums[i] - nums[i - 1]))
        ans = max(ans, abs(nums[0] - nums[-1]))
        return ans

        

s = Solution()
nums = [-5,-10,-5]

print(s.maxAdjacentDistance(nums))  