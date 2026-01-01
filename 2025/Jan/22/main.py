class Solution(object):
    def highestPeak(self, isWater):
        m, n = len(isWater), len(isWater[0])
        res = [[-1 for _ in range(n)] for _ in range(m)]
        queue = []
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    res[i][j] = 0
                    queue.append((i, j))
        while queue:
            i, j = queue.pop(0)
            for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= x < m and 0 <= y < n and res[x][y] == -1:
                    res[x][y] = res[i][j] + 1
                    queue.append((x, y))
        return res
        

if "__main__" == __name__:
    isWater = [[0,1],[0,0]]
    s =  Solution()
    print(s.highestPeak(isWater))