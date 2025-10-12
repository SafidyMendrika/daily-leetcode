from typing import List
import math
from functools import lru_cache

class Solution:
    def magicalSum(self, m: int, k: int, nums: List[int]) -> int:
        MOD = 10**9 + 7 
        @lru_cache(None)
        def dp(m_rem, k_rem, i, flag):
            if m_rem < 0 or k_rem < 0 or m_rem + flag.bit_count() < k_rem:
                return 0
            if m_rem == 0:
                if k_rem == flag.bit_count():
                    return 1
                else:
                    return 0
            if i >= len(nums):
                return 0
            res = 0
            for c in range(m_rem + 1):
                mul = math.comb(m_rem, c) * pow(nums[i], c, MOD) % MOD
                new_flag = flag + c
                res += mul * dp(m_rem - c, k_rem - (new_flag % 2), i + 1, new_flag // 2)
            return res % MOD
        return dp(m, k, 0, 0)
    

solution = Solution()
m = 5
k = 5
nums = [1,10,100,10000,1000000]
print(solution.magicalSum(m, k, nums))