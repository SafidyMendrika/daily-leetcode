class Solution(object):
    def snakesAndLadders(self, board):
        from collections import deque

        n = len(board)

        def get_pos(s):
            quot, rem = divmod(s - 1, n)
            row = n - 1 - quot
            col = rem if quot % 2 == 0 else n - 1 - rem
            return row, col

        visited = set()
        q = deque([(1, 0)])
        while q:
            s, moves = q.popleft()
            if s == n * n:
                return moves
            for i in range(1, 7):
                next_s = s + i
                if next_s > n * n:
                    continue
                r, c = get_pos(next_s)
                if board[r][c] != -1:
                    next_s = board[r][c]
                if next_s not in visited:
                    visited.add(next_s)
                    q.append((next_s, moves + 1))
        return -1


solution = Solution()

board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]

print(solution.snakesAndLadders(board))  