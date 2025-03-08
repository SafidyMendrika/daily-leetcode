import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        
        int k = 7;
        String blocks = "WBBWWBBWBW";

        System.out.println(solution.minimumRecolors(blocks, k));
    }
}
