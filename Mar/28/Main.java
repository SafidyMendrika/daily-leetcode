import java.util.Arrays;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        int[][] grid = {
            {1, 2, 3},
            {2, 5, 7},
            {3, 5, 1}
        };
        int[] queries = {5,6,2};

        System.out.println(Arrays.toString(solution.maxPoints(grid, queries)));
    }
}
