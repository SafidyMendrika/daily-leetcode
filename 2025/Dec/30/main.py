class Solution:
    def check(self, i, j, grid):
        magicSum = grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2]
        sum_ = grid[i][j+2] + grid[i+1][j+1] + grid[i+2][j]
        vis = [False] * 16
        if sum_ != magicSum:
            return False

        for row in range(i, i+3):
            sum_ = grid[row][j] + grid[row][j+1] + grid[row][j+2]
            vis[grid[row][j]] = True
            vis[grid[row][j+1]] = True
            vis[grid[row][j+2]] = True
            if sum_ != magicSum:
                return False

        for col in range(j, j+3):
            sum_ = grid[i][col] + grid[i+1][col] + grid[i+2][col]
            if sum_ != magicSum:
                return False

        for num in range(1, 10):
            if not vis[num]:
                return False

        return True

    def numMagicSquaresInside(self, grid):
        row = len(grid)
        col = len(grid[0])
        count = 0
        for i in range(row - 2):
            for j in range(col - 2):
                if self.check(i, j, grid):
                    count += 1
        return count