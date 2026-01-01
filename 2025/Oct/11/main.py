from typing import List
from collections import Counter
class Solution : 
    def maximumTotalDamage(self, power: List[int]) -> int:
        freq = Counter(power)
        keys = sorted(freq)

        n = len(keys)
        dp = [0] * n
        dp[0] = keys[0]*freq[keys[0]]

        for i in range(1, n):
            val = keys[i]*freq[keys[i]]

            j = i - 1
            while j >= 0 and keys[i] - keys[j] <= 2: j -= 1

            not_take = dp[i - 1]
            take = val + (dp[j] if j >= 0 else 0)

            dp[i] = max(take, not_take)
        
        return dp[-1]
        

solution = Solution()
power = [1,1,3,4]
print(solution.maximumTotalDamage(power))