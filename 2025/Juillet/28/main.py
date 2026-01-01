class Solution:
    def countMaxOrSubsets(self, nums: list[int]) -> int:
        max_or: int = 0
        for num in nums: max_or |= num
        output: int = 0
        n: int = len(nums)
        for mask in range(0, 1 << n):
            or_: int = 0
            for j in range(n):
                if mask & (1 << j): or_ |= nums[j]
            if or_ == max_or: output += 1
        return output
    
solution = Solution()
nums = [3,2,1,5]
print(solution.countMaxOrSubsets(nums))