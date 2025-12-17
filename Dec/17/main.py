from typing import List

class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n=len(prices)
        dp=[[[0 for _ in range(k+1)] for _ in range(3)] for _ in range(n+1)]
        for i in range(3):
            for j in range(k+1):
                if i==1:
                    dp[n][i][j]=-int(1e9)
        for i in range(n+1):
            for j in range(3):
                dp[i][j][k]=0
        for i in range(n-1,-1,-1):
            for b in range(3):
                for t in range(k):
                    profit=dp[i+1][b][t]
                    if b==0:
                        profit=max(profit,-prices[i]+dp[i+1][2][t],prices[i]+dp[i+1][1][t])
                    elif b==1:
                        profit=max(profit,-prices[i]+dp[i+1][0][t+1])
                    else:
                        profit=max(profit,prices[i]+dp[i+1][0][t+1])
                    dp[i][b][t]=profit
        return dp[0][0][0]
    
solution = Solution()
prices = [1,7,9,8,2]
k = 2
print(solution.maximumProfit(prices,k))