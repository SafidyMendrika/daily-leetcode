from typing import List

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        tmp = len(points)
        t_y = []
        con = {}
        mod = 10**9 + 7

        for i in range(tmp):
            y = points[i][1]
            if y not in con:
                con[y] = 1
                t_y.append(y)
            else:
                con[y] += 1

        hor = []
        for y in t_y:
            c = con[y]
            if c >= 2:
            # Use fast formula: C(n, 2) = n*(n-1)//2
                pair = (c * (c - 1)) // 2
                hor.append(pair % mod)

        sum_all = sum(hor) % mod
        sum_sq = sum((h * h) % mod for h in hor) % mod
        total = ((sum_all * sum_all - sum_sq) * pow(2, -1, mod)) % mod

        return total
    
solution = Solution()
points = [[0,0],[1,0],[0,1],[2,1]]
print(solution.countTrapezoids(points))