public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();
        int[][] grid = {
            {0, 2, 1, 0},
            {4, 0, 0, 3},
            {1, 0, 0, 4},
            {0, 3, 2, 0}
        };
        System.out.println(sol.findMaxFish(grid));
        
    }
}
