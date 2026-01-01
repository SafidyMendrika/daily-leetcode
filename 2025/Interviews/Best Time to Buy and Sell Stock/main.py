class Solution(object):
    def maxProfit(self, prices):
        if not prices:
            return 0
        
        n = len(prices)
        dp = [[0] * 2 for _ in range(n)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], -prices[i])
        return dp[n - 1][0]
    
if __name__ == '__main__':
    prices = [7,1,5,3,6,4]
    solution = Solution()
    print(solution.maxProfit(prices))
