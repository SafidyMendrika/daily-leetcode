class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for k in range(1, 61):
            x = num1 - num2 * k
            if x < k:
                return -1
            if k >= x.bit_count():
                return k
        return -1
    
solution = Solution()
num1 = 5
num2 = 7
print(solution.makeTheIntegerZero(num1, num2))