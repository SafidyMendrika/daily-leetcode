class Solution:
    def getNoZeroIntegers(self, n: int) -> list[int]:
        def check(x):
            return '0' not in str(x)

        for i in range(1, n):
            j = n - i
            if check(i) and check(j):
                return [i, j]
            
solution = Solution()
n = 11
print(solution.getNoZeroIntegers(n))