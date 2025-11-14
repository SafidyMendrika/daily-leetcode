class Solution(object):
    def rangeAddQueries(self, n, queries):
        mat = [[0] * (n) for _ in range(n)]

        for top, left, bottom, right in queries:
            mat[top][left] += 1
            if right + 1 < n: 
                mat[top][right + 1] -= 1
            if bottom + 1 < n:
                mat[bottom + 1][left] -= 1
            if bottom + 1 < n and right + 1 < n:
                mat[bottom + 1][right + 1] += 1

        for i in range(n):
            for j in range(1, n):
                mat[i][j] += mat[i][j - 1]
        for j in range(n):
            for i in range(1, n):
                mat[i][j] += mat[i - 1][j]

        return mat
    

solution = Solution()
n = 3
queries = [[1,1,2,2],[0,0,1,1]]
print(solution.rangeAddQueries(n,queries))