import java.util.Arrays;

public class Main {

    public static void main(String[] args) {
        Solution s = new Solution();
        int [][] grid = {{1,3},{2,2}};

        System.out.println(Arrays.toString(s.findMissingAndRepeatedValues(grid)));
    }
}