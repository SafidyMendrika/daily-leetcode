import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        
        int n = 5;
        int[][] edges = {{0,1,7}, {1,3,7}, {1,2,1}};
        int[][] query = {{0,3}, {3,4}};
        int[] result = solution.minimumCost(n, edges, query);
        System.out.println( Arrays.toString(result));
    }
}
