class Solution:
    def maximumUniqueSubarray(self, nums: list[int]) -> int:
        n = len(nums)

        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]

        last_seen = [0] * 10001  

        left = 0
        max_sum = 0
        for right in range(1, n + 1):
            val = nums[right - 1]

            left = max(left, last_seen[val])

            max_sum = max(max_sum, prefix_sum[right] - prefix_sum[left])

            last_seen[val] = right

        return max_sum
    
solution = Solution()
nums = [4,2,4,5,6]
print(solution.maximumUniqueSubarray(nums))