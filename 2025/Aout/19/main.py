class Solution:
    def zeroFilledSubarray(self, nums: list[int]) -> int:
        start = -1
        count = 0
        nums.append(-1)
        for i in range(len(nums)):
            if nums[i] == 0 and start==-1:
                start = i
            if nums[i]!=0 and start!=-1:
                n = i-start
                start = -1
                count += n*(n+1)//2
        return count

solution = Solution()
nums = [1,3,0,0,2,0,0,4]
print(solution.zeroFilledSubarray(nums))  