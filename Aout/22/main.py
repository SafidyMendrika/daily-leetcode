class Solution:
    def minimumArea(self, grid: list[list[int]]) -> int:
        n, m = len(grid), len(grid[0])
        min_row, max_row, min_col, max_col = n, -1, m, -1

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    min_row = min(min_row, i)
                    max_row = max(max_row, i)
                    min_col = min(min_col, j)
                    max_col = max(max_col, j)

        height = max_row - min_row + 1
        width  = max_col - min_col + 1
        return height * width
    

solution = Solution()
grid = [[0,1,0],[1,0,1]]
print(solution.minimumArea(grid))