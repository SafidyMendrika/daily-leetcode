from typing import List

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        total = sum(nums)
        rem = total%p
        if rem == 0: 
            return 0
        curr = 0
        ans = n
        mp = {0: 0}  

        for i in range(1, n + 1):
            curr = (curr + nums[i - 1]) % p
            target = (curr - rem + p) % p

            if target in mp:
                length = i - mp[target]
                if length < ans:
                    ans = length

            mp[curr] = i

        return ans if ans < n else -1
    
solution = Solution()
nums = [3,1,4,2]
p = 6
print(solution.minSubarray(nums,p))