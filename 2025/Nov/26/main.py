from typing import List

class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        MOD = 10**9 + 7
        m,n = len(grid), len(grid[0])
        dp = [[[0]* k for _ in range(n+1)] for _ in range(m+1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                curr = grid[i - 1][j - 1] % k   
                if i == 1 and j == 1:
                    dp[i][j][curr] = 1
                else:
                    for h in range(k):
                        prev = k + h - curr if h < curr else h - curr  
                        dp[i][j][h] = (dp[i - 1][j][prev] + dp[i][j - 1][prev]) % MOD
        
        return dp[-1][-1][0]
    

solution = Solution()
grid = [[5,2,4],[3,0,5],[0,7,2]]
k = 3
print(solution.numberOfPaths(grid,k))