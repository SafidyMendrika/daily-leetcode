class Solution:
    def largestIsland(self, grid: list[list[int]]) -> int:
        n = len(grid)
        island_sizes = {}
        island_id = 2 
        
        def is_valid(x: int, y: int) -> bool:
            return 0 <= x < n and 0 <= y < n
        
        def dfs(row: int, col: int, id: int) -> int:
            if not is_valid(row, col) or grid[row][col] != 1:
                return 0
            
            grid[row][col] = id
            size = 1
            
            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                new_row, new_col = row + dx, col + dy
                size += dfs(new_row, new_col, id)
            
            return size
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    size = dfs(i, j, island_id)
                    island_sizes[island_id] = size
                    island_id += 1
        
        if not island_sizes:
            return 1
        
        if len(island_sizes) == 1 and island_sizes[list(island_sizes.keys())[0]] == n * n:
            return n * n
        
        max_size = max(island_sizes.values()) if island_sizes else 0
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    neighbor_ids = set()
                    for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                        new_i, new_j = i + dx, j + dy
                        if is_valid(new_i, new_j) and grid[new_i][new_j] > 1:
                            neighbor_ids.add(grid[new_i][new_j])
                    
                    current_size = 1  
                    for id in neighbor_ids:
                        current_size += island_sizes[id]
                    
                    max_size = max(max_size, current_size)
        
        return max_size
    
if __name__ == "__main__":
    grid = [[1,0],[0,1]]
    s = Solution()
    print(s.largestIsland(grid))