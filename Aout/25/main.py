class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        if not mat or not mat[0]:
            return []
        
        m, n = len(mat), len(mat[0])
        result = [0] * (m * n)
        row, col = 0, 0
        up = True
        
        for i in range(m * n):
            result[i] = mat[row][col]
            
            if up:
                if col == n - 1:  
                    row += 1
                    up = False
                elif row == 0: 
                    col += 1
                    up = False
                else:  
                    row -= 1
                    col += 1
            else: 
                if row == m - 1: 
                    col += 1
                    up = True
                elif col == 0: 
                    row += 1
                    up = True
                else:  
                    row += 1
                    col -= 1
                    
        return result

solution = Solution()
mat = [[1,2,3],[4,5,6],[7,8,9]]
print(solution.findDiagonalOrder(mat))