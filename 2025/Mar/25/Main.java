
public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        
        int n = 10;
        int[][] rectangles = {{1,0,5,2},{0,2,2,4},{3,2,5,3},{0,4,4,5}};
        
        System.out.println(solution.checkValidCuts(n, rectangles));
    }
}
