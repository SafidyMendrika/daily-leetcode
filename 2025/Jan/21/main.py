class Solution(object):
    def gridGame(self, grid):
        n = len(grid[0])
        prefix = [[0] * n for _ in range(2)]
        prefix[0][0] = grid[0][0]
        prefix[1][0] = grid[1][0]
        for i in range(1, n):
            prefix[0][i] = prefix[0][i - 1] + grid[0][i]
            prefix[1][i] = prefix[1][i - 1] + grid[1][i]
        res = float('inf')
        for i in range(n):
            a = prefix[0][-1] - prefix[0][i]
            b = 0 if i == 0 else prefix[1][i - 1]
            res = min(res, max(a, b))
        return res
        

if __name__ == '__main__':
    grid = [[2,5,4],[1,5,1]]
    s = Solution()
    print(s.gridGame(grid))