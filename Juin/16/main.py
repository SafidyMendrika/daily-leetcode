class Solution:
    def maximumDifference(self, nums: list[int]) -> int:
        ans = -1
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    ans = max(ans, nums[j] - nums[i])
        return ans
    
s = Solution()
nums = nums = [7,1,5,4]

print(s.maximumDifference(nums))