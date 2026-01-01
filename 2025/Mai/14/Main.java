import java.util.List;

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        
        String s = "abcyy";
        int t = 2;
        List<Integer> nums = List.of(1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2);
        System.out.println(solution.lengthAfterTransformations(s, t,nums));

    }   
}