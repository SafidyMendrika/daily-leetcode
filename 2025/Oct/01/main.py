class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = 0
        empty = 0
        while numBottles:
            ans += numBottles
            empty += numBottles
            numBottles = (empty) // numExchange
            empty = empty % numExchange
        return ans
        

solution = Solution()
numBottles = 15
numExchange = 4
print(solution.numWaterBottles(numBottles,numExchange))