class Solution:
    def lenOfVDiagonal(self, grid: list[list[int]]) -> int:

        R, C = len(grid), len(grid[0])


        directions = [
            (-1, -1), 
            (-1, 1),  
            (1, 1), 
            (1, -1)  
        ]

        memo = dict()

        def dfs(i, j, d, can_turn):
            state = (i, j, d, can_turn)
            if state in memo:
                return memo[state]

            target = 0 if grid[i][j] == 2 else 2

            next_steps = [(d, can_turn)]
            if can_turn:
                next_steps.append(((d + 1) % 4, False)) 

            max_len = 1
            for nd, t in next_steps:
                di, dj = directions[nd]
                ni, nj = i + di, j + dj
                if 0 <= ni < R and 0 <= nj < C and grid[ni][nj] == target:
                    max_len = max(max_len, 1 + dfs(ni, nj, nd, t))

            memo[state] = max_len
            return memo[state]

        best = 0
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    for d in range(4):
                        best = max(best, dfs(i, j, d, True))
        
        return best
    
soution = Solution()
grid = [[2,2,1,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]]
print(soution.lenOfVDiagonal(grid))  