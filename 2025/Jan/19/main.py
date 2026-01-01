import heapq

class Solution(object):
    def trapRainWater(self, heightMap : list[list[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0
        m, n = len(heightMap), len(heightMap[0])
        visited = [[0] * n for _ in range(m)]
        heap = []
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    visited[i][j] = 1
        res = 0
        while heap:
            h, i, j = heapq.heappop(heap)
            for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= x < m and 0 <= y < n and not visited[x][y]:
                    res += max(0, h - heightMap[x][y])
                    heapq.heappush(heap, (max(h, heightMap[x][y]), x, y))
                    visited[x][y] = 1
        return res

        

if __name__ == '__main__':
    heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
    s = Solution()
    print(s.trapRainWater(heightMap))