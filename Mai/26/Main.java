public class Main {

    public static void main(String[] args) {
        Solution solution = new Solution();
        String colors = "abaca";
        int[][] edges = {{0,1},{0,2},{2,3},{3,4}};

        System.out.println(solution.largestPathValue(colors, edges));
    }
}