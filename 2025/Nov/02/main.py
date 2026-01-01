from typing import List

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        WALL_OR_GUARD = 1
        GUARDED = -1
        grid = [[0] * n for _ in range(m)]

        for r, c in walls + guards:
            grid[r][c] = WALL_OR_GUARD

        for r, c in guards:
            for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                nr, nc = r + dr, c + dc
                while 0 <= nr < m and 0 <= nc < n and grid[nr][nc] != WALL_OR_GUARD:
                    grid[nr][nc] = GUARDED
                    nr += dr
                    nc += dc

        return sum(cell == 0 for row in grid for cell in row)

solution = Solution()
m = 4
n = 6
guards = [[0,0],[1,1],[2,3]]
walls = [[0,1],[2,2],[1,4]]
print(solution.countUnguarded(m,n,guards,walls))


