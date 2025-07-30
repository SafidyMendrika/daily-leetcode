
class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        max_val = max(nums)
        
        count = 1
        max_count = 1
        for i in range(1, len(nums)):
            if nums[i] >= max_val and nums[i - 1] == nums[i]:
                count += 1
            elif nums[i] == max_val:
                count = 1
            else:
                count = 0
            max_count = max(max_count, count)
        
        return max_count
    
solution = Solution()
nums = [1,2,3,3,2,2]
print(solution.longestSubarray(nums))