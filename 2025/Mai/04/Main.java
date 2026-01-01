
public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        
        int[][] dominoes = {{1,2},{1,2},{1,1},{1,2},{2,2}};

        System.out.println(solution.numEquivDominoPairs(dominoes)); 

    }   
}