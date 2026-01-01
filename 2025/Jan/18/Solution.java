import java.util.Arrays;
import java.util.Comparator;
import java.util.PriorityQueue;

public class Solution {

    public int minCost(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        int[][] cost = new int[m][n];
        for (int[] row : cost) {
            Arrays.fill(row, Integer.MAX_VALUE);
        }
        cost[0][0] = 0;
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[2]));
        pq.offer(new int[]{0, 0, 0});
        int[][] directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        
        while (!pq.isEmpty()) {
            int[] current = pq.poll();
            int x = current[0], y = current[1], c = current[2];
            if (x == m - 1 && y == n - 1) {
                return c;
            }
            for (int i = 0; i < 4; i++) {
                int nx = x + directions[i][0];
                int ny = y + directions[i][1];
                int nc = c + (grid[x][y] == i + 1 ? 0 : 1);
                if (nx >= 0 && nx < m && ny >= 0 && ny < n && nc < cost[nx][ny]) {
                    cost[nx][ny] = nc;
                    pq.offer(new int[]{nx, ny, nc});
                }
            }
        }
        return -1;
    }
}