from typing import List
from sortedcontainers import SortedList

class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        dp=[0]*(len(nums)+1)
        dp[0]=1
        currsum=1
        l=0
        curr=SortedList()
        mod=10**9+7
        for i,el in enumerate(nums):
            curr.add(el)
            while l<len(nums) and curr[-1]-curr[0]>k:
                currsum=(currsum-dp[l])%mod
                curr.remove(nums[l])
                l+=1
            dp[i+1]=currsum
            currsum=(currsum+dp[i+1])%mod
        return dp[-1]
    

solution = Solution()
nums = [9,4,1,3,7] 
k = 4
print(solution.countPartitions(nums,k))