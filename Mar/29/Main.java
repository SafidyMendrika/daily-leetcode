import java.util.List;

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        List<Integer> nums = List.of(8,3,9,3,8);
        int k = 2;
        System.out.println(solution.maximumScore(nums, k));
    }
}
