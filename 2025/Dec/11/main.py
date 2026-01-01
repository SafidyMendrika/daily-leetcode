from typing import List

class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:

        ans = 0
        X, Y = {}, {}
        for i, j in buildings:
            if i not in X: X[i] = [j, j]
            else:
                if j < X[i][0]: X[i][0] = j
                if j > X[i][1]: X[i][1] = j
            if j not in Y: Y[j] = [i, i]
            else:
                if i < Y[j][0]: Y[j][0] = i
                if i > Y[j][1]: Y[j][1] = i
        for i, j in buildings:
            if X[i][0] < j < X[i][1] and Y[j][0] < i < Y[j][1]:
                ans += 1
        return ans
    

solution = Solution()
n = 3
buildings = [[1,2],[2,2],[3,2],[2,1],[2,3]]
print(solution.countCoveredBuildings(n,buildings))