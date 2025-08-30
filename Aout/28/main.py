from typing import List

class Solution:
    def sortMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])

        def reverse(arr):
            i, j = 0, len(arr) - 1
            while i < j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1

        def sort_diagonal(row, col, increasing):
            length = min(rows - row, cols - col)
            diagonal = [mat[row + i][col + i] for i in range(length)]
            diagonal.sort()
            if not increasing:
                reverse(diagonal)
            for i in range(length):
                mat[row + i][col + i] = diagonal[i]

        for row in range(rows):
            sort_diagonal(row, 0, False)  

        for col in range(1, cols):
            sort_diagonal(0, col, True)  

        return mat

solution = Solution()
grid = [[1,7,3],[9,8,2],[4,5,6]]
print(solution.sortMatrix(grid))  