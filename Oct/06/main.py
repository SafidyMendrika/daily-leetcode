from typing import List
import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        visit = set([(0,0)])

        start = (grid[0][0], 0, 0)
        minHeap = []
        heapq.heapify(minHeap)
        heapq.heappush(minHeap, start)

        res = 0
        while minHeap:
            cur,r,c = heapq.heappop(minHeap)
            res = max(res,cur)
            if r == c == n-1:
                return res
            for dr,dc in directions:
                a = r+dr
                b = c+dc
                if (
                    ( (a,b) in visit) or
                    (a < 0 or b < 0) or
                    (a == n or b == n)
                ):
                    continue
                visit.add( (a,b) )
                val = (grid[a][b], a,b)        
                heapq.heappush(minHeap, val) 

            
solution = Solution()
grid = [[0,2],[1,3]]
print(solution.swimInWater(grid))  