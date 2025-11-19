class Solution:
    def findFinalValue(self, nums, original):
        cnt = [0] * 1001
        for x in nums:
            cnt[x] += 1

        while original <= 1000 and cnt[original] > 0:
            original *= 2

        return original
    
solution = Solution()
nums = [5,3,6,1,12]
original = 3
print(solution.findFinalValue(nums,original))