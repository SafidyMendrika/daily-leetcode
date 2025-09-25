from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        for i in range(1,n):
            for j in range(len(triangle[i])):
                if j == 0:
                    best_above = triangle[i-1][j]
                elif j==len(triangle[i])-1:
                    best_above = triangle[i-1][j-1]
                else:
                    best_above = min(triangle[i-1][j], triangle[i-1][j-1])
                triangle[i][j] +=  best_above
        return min(triangle[-1])    