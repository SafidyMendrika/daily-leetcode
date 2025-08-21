class Solution:
    def countSquares(self, matrix: list[list[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        dp = [[0] * cols for _ in range(rows)]
        cnt = 0
        for j in range(cols):
            if matrix[0][j] == 1:
                dp[0][j] = 1
                cnt += dp[0][j]


        for i in range(1, rows):
            if matrix[i][0] == 1:
                dp[i][0] = 1
                cnt += dp[i][0]
        

        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 1:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
                    cnt += dp[i][j]
        return cnt
    
solution = Solution()
matrix =[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
print(solution.countSquares(matrix))