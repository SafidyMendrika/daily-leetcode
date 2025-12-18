from typing import List

class Solution:
    def maxProfit(self, prices : List[int], strategy : List[int], k : int):
        n = len(prices)

        base = sum(strategy[i] * prices[i] for i in range(n))

        pref_price = [0] * (n + 1)
        pref_profit = [0] * (n + 1)

        for i in range(n):
            pref_price[i + 1] = pref_price[i] + prices[i]
            pref_profit[i + 1] = pref_profit[i] + strategy[i] * prices[i]

        best_delta = 0
        half = k // 2

        for l in range(n - k + 1):
            m = l + half
            r = l + k

            old_profit = pref_profit[r] - pref_profit[l]
            new_profit = pref_price[r] - pref_price[m]

            best_delta = max(best_delta, new_profit - old_profit)

        return base + best_delta

solution = Solution()
prices = [4,2,8]
strategy = [-1,0,1]
k = 2
print(solution.maxProfit(prices,strategy,k))