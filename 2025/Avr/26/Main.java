
public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        
        int[] nums = {1, 3, 5, 2, 7, 5};
        int minK = 1;
        int maxK = 5;

        System.out.println(solution.countSubarrays(nums, minK, maxK));

    }   
}