class Solution(object):
    def firstCompleteIndex(self, arr, mat):
        m, n = len(mat), len(mat[0])
        row_count = [0] * m
        col_count = [0] * n
        position = {}

        for i in range(m):
            for j in range(n):
                position[mat[i][j]] = (i, j)

        for idx, num in enumerate(arr):
            i, j = position[num]
            row_count[i] += 1
            col_count[j] += 1

            if row_count[i] == n or col_count[j] == m:
                return idx

        return -1
    
if __name__ == '__main__':
    sol = Solution()
    arr =  [1,3,4,2]
    mat = [[1,4],[2,3]]
    print(sol.firstCompleteIndex(arr, mat))