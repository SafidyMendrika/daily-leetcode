public class Main {
    public static void main(String[] args) {
        int[][] grid = {{1, 1, 1, 1}, {2, 2, 2, 2}, {1, 1, 1, 1}, {2, 2, 2, 2}};

        Solution solution = new Solution();
        System.out.println(solution.minCost(grid));
    }
}
