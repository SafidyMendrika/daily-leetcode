from typing import List

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        uf = {}
        left,right = {},{}
        water = {}

        def find(i):
            if i not in uf:
                uf[i] = i
                left[i] = right[i] = cells[i][1]
            return i if uf[i] == i else find(uf[i])
        
        for i,(r,c) in enumerate(cells):
            pi = find(i)
            for pj in map(find,[water[(r+dr, c+dc)] for dr,dc in product([-1,0,1], repeat=2) if (r+dr,c+dc) in water]):
                uf[pj] = pi
                left[pi] = min(left[pi],left[pj])
                right[pi] = max(right[pi], right[pj])
            water[(r,c)] = i
            if left[pi] == 1 and right[pi] == col:
                break
        return i
        
         

solution = Solution()
row = 2
col = 2
cells = [[1,1],[2,1],[1,2],[2,2]]
print(solution.latestDayToCross(row,col,cells))