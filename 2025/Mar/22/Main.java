
public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        
        int n = 6;
        int[][] edges = {{0, 1}, {0, 2}, {1, 2}, {3, 4}};
        int result = solution.countCompleteComponents(n, edges);
        System.out.println(result); 
    }
}
