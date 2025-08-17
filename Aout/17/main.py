class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        dp: list[float] = [0] * (n + 1)
        dp[0] = 1
        cur_prob: float = int(bool(k))
        for i in range(1, n + 1):
            dp[i] = cur_prob / maxPts
            if i < k: cur_prob += dp[i]
            if i - maxPts >= 0 and i - maxPts < k: cur_prob -= dp[i - maxPts]
        return sum(dp[k:])
    
solution = Solution()
n = 10
k = 1
maxPts = 10
print(solution.new21Game(n, k, maxPts))