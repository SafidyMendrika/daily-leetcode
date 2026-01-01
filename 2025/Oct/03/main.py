from typing import List
import heapq

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        pq = []
        n, m = len(heightMap), len(heightMap[0])
        visited = set()
        for j in range(m):
            heapq.heappush(pq, (heightMap[0][j], 0, j, heightMap[0][j]))
            heapq.heappush(pq, (heightMap[n-1][j], n-1, j, heightMap[n-1][j]))
            visited.add((0, j))
            visited.add((n-1, j))
        
        for i in range(1, n-1):
            heapq.heappush(pq, (heightMap[i][0], i, 0, heightMap[i][0]))
            heapq.heappush(pq, (heightMap[i][m-1], i, m-1, heightMap[i][m-1]))
            visited.add((i, 0))
            visited.add((i, m-1))
        res = 0

        def neighbors(i, j):
            temp = []
            directions = [(0, -1), (-1, 0), (1, 0), (0, 1)]
            for dr, dc in directions:
                r, c = i+dr, j+dc
                if 0 <= r < n and 0 <= c < m:
                    temp.append((r, c))
            return temp

        while pq:
            h, i, j, b = heapq.heappop(pq)
            if i != 0 and j != m-1:
                res += b-h if b > h else 0
            for x, y in neighbors(i, j):
                if (x, y) not in visited:
                    heapq.heappush(pq, (heightMap[x][y], x, y, max(b, heightMap[x][y])))
                    visited.add((x, y))

        return res


solution = Solution()
heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
print(solution.trapRainWater(heightMap))  