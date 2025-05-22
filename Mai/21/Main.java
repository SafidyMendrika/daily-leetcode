import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        
        Solution solution = new Solution();
        int[][] matrix = {{0,1,2,0},{3,4,5,2},{1,3,1,5}};
        solution.setZeroes(matrix);
        System.out.println(Arrays.deepToString(matrix));
        

    }   
}