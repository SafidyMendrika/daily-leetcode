class Solution:
    def maxSum(self, nums: list[int]) -> int:
        unique_nums = set(nums)
        positive_sum,negative_count = 0,0 

        for num in unique_nums:
            if num >= 0 :
                positive_sum += num
            else:
                negative_count += 1

        if len(unique_nums) ==  negative_count:
            return max(unique_nums)
        return positive_sum

solution = Solution()
nums = [1,2,-1,-2,1,0,-1]
print(solution.maxSum(nums))