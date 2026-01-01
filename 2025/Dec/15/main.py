from typing import List

class Solution:
    def getDescentPeriods(self, prices : List[int]):
        ans = 1
        cnt = 1

        for i in range(1, len(prices)):
            if prices[i] == prices[i - 1] - 1:
                cnt += 1
            else:
                cnt = 1
            ans += cnt

        return ans
    
solution = Solution()
prices = [3,2,1,4]
print(solution.getDescentPeriods(prices))