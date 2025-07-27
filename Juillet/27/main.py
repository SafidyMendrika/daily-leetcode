class Solution:
    def countHillValley(self, nums: list[int]) -> int:
        count = 0
        n = len(nums)
        for i in range(1, n - 1):
            if nums[i] == nums[i - 1]:
                continue
            left = i - 1
            while left >= 0 and nums[left] == nums[i]:
                left -= 1
            right = i + 1
            while right < n and nums[right] == nums[i]:
                right += 1
            if left >= 0 and right < n:
                if nums[left] < nums[i] and nums[right] < nums[i]:
                    count += 1
                elif nums[left] > nums[i] and nums[right] > nums[i]:
                    count += 1
        return count
    

solution = Solution()
nums = [2,4,1,1,6,5]
print(solution.countHillValley(nums))