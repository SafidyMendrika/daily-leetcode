import java.util.*;

class Solution {
    public int[] maxPoints(int[][] grid, int[] queries) {
        int m = grid.length, n = grid[0].length;
        int k = queries.length;
        int[] result = new int[k];

        int[][] sortedQueries = new int[k][2];
        for (int i = 0; i < k; i++) {
            sortedQueries[i] = new int[]{queries[i], i};
        }
        Arrays.sort(sortedQueries, Comparator.comparingInt(a -> a[0]));

        PriorityQueue<int[]> minHeap = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        minHeap.offer(new int[]{grid[0][0], 0, 0});
        
        boolean[][] visited = new boolean[m][n];
        visited[0][0] = true;

        int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

        int count = 0; 
        int maxValue = 0; 

        for (int[] query : sortedQueries) {
            int qValue = query[0], index = query[1];

            while (!minHeap.isEmpty() && minHeap.peek()[0] < qValue) {
                int[] cell = minHeap.poll();
                maxValue = cell[0];
                int x = cell[1], y = cell[2];
                count++;

                for (int[] dir : directions) {
                    int nx = x + dir[0], ny = y + dir[1];
                    if (nx >= 0 && nx < m && ny >= 0 && ny < n && !visited[nx][ny]) {
                        visited[nx][ny] = true;
                        minHeap.offer(new int[]{grid[nx][ny], nx, ny});
                    }
                }
            }

            result[index] = count;
        }

        return result;
    }
}
