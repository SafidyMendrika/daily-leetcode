class Solution(object):
    def maxProfit(self, prices):
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                max_profit += prices[i] - prices[i-1]
        return max_profit

if "__main__" == __name__ : 
    s = Solution()
    prices = [7,1,5,3,6,4]
    print(s.maxProfit(prices))

        