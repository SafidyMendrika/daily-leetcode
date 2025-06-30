class Solution:
    def findLHS(self, nums: list[int]) -> int:
        nums.sort() 
        j = 0
        ans = 0

        for i in range(len(nums)):
            while nums[i] - nums[j] > 1:
                j += 1

            if nums[i] - nums[j] == 1:
                ans = max(ans, i - j + 1)

        return ans
    
solution = Solution()
nums = [1,2,3,4]
print(solution.findLHS(nums)) 