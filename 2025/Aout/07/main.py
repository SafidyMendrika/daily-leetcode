class Solution:
    def maxCollectedFruits(self, fruits: list[list[int]]) -> int:
        output: int = 0
        n: int = len(fruits)
        for i in range(n):
            output += fruits[i][i]
            fruits[i][i] = 0
        bound: int = n // 2
        prev_bound: int = 0
        for i in range(n):
            lower_bound: int = max(i + 1, -(i - n) - 1, bound)
            for j in range(n - 1, lower_bound - 1, -1):
                fruits[i][j] += max(
                    (fruits[i - 1][j - 1] if (i - 1 >= 0 and j - 1 >= prev_bound) else 0),
                    (fruits[i - 1][j] if (i - 1 >= 0 and j >= prev_bound) else 0),
                    (fruits[i - 1][j + 1] if (i - 1 >= 0 and j + 1 < n) else 0)
                )
            prev_bound = lower_bound
        output += fruits[n - 2][n - 1]
        prev_bound = 0
        for j in range(n):
            lower_bound: int = max(j + 1, -(j - n) - 1, bound)
            for i in range(n - 1, lower_bound - 1, -1):
                fruits[i][j] += max(
                    (fruits[i - 1][j - 1] if (j - 1 >= 0 and i - 1 >= prev_bound) else 0),
                    (fruits[i][j - 1] if (j - 1 >= 0 and i >= prev_bound) else 0),
                    (fruits[i + 1][j - 1] if (j - 1 >= 0 and i + 1 < n) else 0)
                )
            prev_bound = lower_bound
        output += fruits[n - 1][n - 2]
        return output
    
solution = Solution()
fruits = [[1,2,3,4],[5,6,8,7],[9,10,11,12],[13,14,15,16]]
print(solution.maxCollectedFruits(fruits))