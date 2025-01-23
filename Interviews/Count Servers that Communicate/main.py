class Solution(object):
    def countServers(self, grid):
        row, col = len(grid), len(grid[0])
        row_cnt = [0] * row
        col_cnt = [0] * col
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    row_cnt[i] += 1
                    col_cnt[j] += 1
        res = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1 and (row_cnt[i] > 1 or col_cnt[j] > 1):
                    res += 1
        return res
        

if "__main__" == __name__:
    grid = [[1,0],[0,1]]
    s = Solution()
    print(s.countServers(grid))