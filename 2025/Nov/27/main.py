from typing import List

class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n == k: return sum(nums)
        if n < k * 2:
            return max(sum(nums[i:i + k]) for i in range(n - k + 1))

        cs = sum(nums[:k])
        pref = [cs]
        for i in range(k, n):
            cs += nums[i]
            cs -= nums[i - k]
            pref.append(cs)
        
        ans = -(10 ** 18)
        for i in range(k):
            cur = pref[i]
            ans = max(ans, cur)
            for j in range(i + k, len(pref), k):
                cur = max(cur, 0) + pref[j]
                ans = max(ans, cur)
        return ans
    
solution = Solution()
nums = [1,2]
k = 1
print(solution.maxSubarraySum(nums,k))