class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        preCount=curCount=ans=0
        for i in nums:
            if i==1: curCount+=1
            else:
                ans=max(ans,preCount+curCount)
                preCount=curCount
                curCount=0
        ans=max(ans,preCount+curCount)
        return ans if len(nums)!=ans else len(nums)-1
    
solution = Solution()
nums = [0,1,1,1,0,1,1,0,1]
print(solution.longestSubarray(nums)) 