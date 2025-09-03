class Solution:
    def numberOfPairs(self, points: list[list[int]]) -> int:
        n = len(points)
        cnt = 0

        points.sort(key=lambda x: (x[0], -x[1]))

        for i in range(n):
            x1, y1 = points[i]
            maxi = float('-inf')

            for j in range(i + 1, n):
                x2, y2 = points[j]

                if y2 > y1:
                    continue  

                if y2 > maxi:
                    maxi = y2
                    cnt += 1

        return cnt


solution = Solution()
points = [[6,2],[4,4],[2,6]]
print(solution.numberOfPairs(points))  