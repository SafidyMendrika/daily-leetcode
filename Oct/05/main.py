from collections import deque
class Solution:
    dir = [[0,1], [1,0], [0,-1], [-1,0]]
    
    def bfs(self, q, vis, heights):
        n, m = len(heights), len(heights[0])
        while q:
            x, y = q.popleft()
            for dx, dy in self.dir:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and heights[nx][ny] >= heights[x][y] and vis[nx][ny] == 0:
                    q.append((nx, ny))
                    vis[nx][ny] = 1

    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        n, m = len(heights), len(heights[0])
        pacific = [[0]*m for _ in range(n)]
        atlantic = [[0]*m for _ in range(n)]
        qPacific, qAtlantic = deque(), deque()
        
        for i in range(n):
            qPacific.append((i, 0))
            pacific[i][0] = 1
        for j in range(m):
            qPacific.append((0, j))
            pacific[0][j] = 1
        
        for i in range(n):
            qAtlantic.append((i, m-1))
            atlantic[i][m-1] = 1
        for j in range(m):
            qAtlantic.append((n-1, j))
            atlantic[n-1][j] = 1

        self.bfs(qPacific, pacific, heights)
        self.bfs(qAtlantic, atlantic, heights)

        result = []
        for i in range(n):
            for j in range(m):
                if pacific[i][j] and atlantic[i][j]:
                    result.append([i, j])
        
        return result
    
solution = Solution()
heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
print(solution.pacificAtlantic(heights))